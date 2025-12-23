import React, { useState } from "react";
import { ArrowRight, Loader2, Bot } from "lucide-react";
import ReactMarkdown from "react-markdown";
import "./FullPageChatbot.css";

export default function FullPageChatbot() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSend = async () => {
    if (!prompt.trim()) return;

    setLoading(true);
    setResponse(null);
    setError("");

    try {
      // 1. Point to the new endpoint defined in routes.py
      const res = await fetch("http://localhost:8000/research", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        // 2. Send 'query' because routes.py defines class ResearchRequest(BaseModel): query: str
        body: JSON.stringify({ query: prompt }),
      });

      if (!res.ok) throw new Error("Failed to fetch response");

      const data = await res.json();

      // 3. Robust Output Handling:
      // We check common keys since we haven't seen the Orchestrator code.
      // It usually returns 'final_report', 'report', 'output', or just 'result'.
      const outputText =
        data.final_report ||
        data.report ||
        data.output ||
        data.result ||
        data.answer;

      if (outputText) {
        setResponse(outputText);
      } else {
        // Fallback: If output is complex, stringify it so we can see what's happening
        setResponse(
          typeof data === "string" ? data : JSON.stringify(data, null, 2)
        );
      }
    } catch (err) {
      setError("Error connecting to server. Is the backend running?");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !loading) handleSend();
  };

  return (
    <section className="full-chatbot-section">
      <div className="chatbot-content-center">
        <h1 className="chatbot-main-title">What’s on your mind?</h1>

        <div
          className={`chatbot-input-container ${
            loading ? "loading-state" : ""
          }`}
        >
          <input
            type="text"
            className="chatbot-input-field"
            placeholder="Type your prompt here..."
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={loading}
          />
          <button
            className="chatbot-send-button"
            onClick={handleSend}
            disabled={loading}
          >
            {loading ? (
              <Loader2 size={24} className="spin-anim" color="#E0AAFF" />
            ) : (
              <ArrowRight size={24} color="white" />
            )}
          </button>
        </div>

        {loading && (
          <div className="loading-indicator">
            <Bot size={20} className="pulse-anim" />
            <span>Researching and analyzing sources...</span>
          </div>
        )}

        {error && <div className="error-message">{error}</div>}

        {response && (
          <div className="response-container">
            <div className="response-content">
              <ReactMarkdown>{response}</ReactMarkdown>
            </div>
          </div>
        )}
      </div>
    </section>
  );
}
