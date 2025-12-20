import React, { useState } from "react";
import { ArrowRight } from "lucide-react";
import "./FullPageChatbot.css";

export default function FullPageChatbot() {
  const [prompt, setPrompt] = useState("");

  return (
    <section className="full-chatbot-section">
      <div className="chatbot-content-center">
        {/* Reverted back to standard H1 */}
        <h1 className="chatbot-main-title">What’s on your mind?</h1>

        {/* Input Bar Container */}
        <div className="chatbot-input-container">
          <input
            type="text"
            className="chatbot-input-field"
            placeholder="Type your prompt here"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
          />
          <button className="chatbot-send-button">
            <ArrowRight size={24} color="white" />
          </button>
        </div>
      </div>
    </section>
  );
}
