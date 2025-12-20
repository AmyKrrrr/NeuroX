import React, { useState, useEffect } from "react";
import "./HeroChatbot.css";
import { Send, Bot, User, Sparkles } from "lucide-react";

const PROMPT_TEXT = "Impact of AI in the Tech Market (2025).";

// Research paper style output with line breaks
const RESPONSE_TEXT = `MARKET ANALYSIS: AI INTEGRATION [2025]

1. EXECUTIVE SUMMARY
AI adoption has accelerated sector valuation by 42% YoY. Primary drivers include generative models in SaaS and autonomous hardware.

2. KEY METRICS
• Semiconductor Demand: +210% (GPU focus)
• Cloud Infrastructure: $580B projected cap
• Labor Shift: 15% workforce reallocation to prompt engineering

3. CONCLUSION
Market volatility remains high, but long-term trajectory indicates a fundamental shift in software architecture and silicon dependency.`;

export default function HeroChatbot() {
  const [step, setStep] = useState("idle"); // idle, typing, processing, responding, finished
  const [inputValue, setInputValue] = useState("");
  const [messages, setMessages] = useState([]);
  const [responseBuffer, setResponseBuffer] = useState("");

  useEffect(() => {
    let timeout;

    // CYCLE START: Wait a bit then start typing
    if (step === "idle") {
      timeout = setTimeout(() => setStep("typing"), 1000);
    }

    // STEP 1: Type the prompt into the input
    if (step === "typing") {
      if (inputValue.length < PROMPT_TEXT.length) {
        timeout = setTimeout(() => {
          setInputValue(PROMPT_TEXT.slice(0, inputValue.length + 1));
        }, 40); // Slightly faster typing for the prompt
      } else {
        timeout = setTimeout(() => {
          setMessages([{ role: "user", content: PROMPT_TEXT }]);
          setInputValue("");
          setStep("processing");
        }, 600);
      }
    }

    // STEP 2: Processing (Fake loading delay)
    if (step === "processing") {
      timeout = setTimeout(() => setStep("responding"), 1500);
    }

    // STEP 3: Stream the AI response
    if (step === "responding") {
      if (responseBuffer.length < RESPONSE_TEXT.length) {
        // Variable speed typing to simulate "thinking"
        const delay = Math.random() * 20 + 10;
        timeout = setTimeout(() => {
          setResponseBuffer(RESPONSE_TEXT.slice(0, responseBuffer.length + 1));
        }, delay);
      } else {
        timeout = setTimeout(() => setStep("finished"), 4000); // Read time
      }
    }

    // STEP 4: Finished state (wait then reset)
    if (step === "finished") {
      timeout = setTimeout(() => {
        setMessages([]);
        setResponseBuffer("");
        setStep("idle");
      }, 1000);
    }

    return () => clearTimeout(timeout);
  }, [step, inputValue, responseBuffer]);

  return (
    <div className="chatbot-window">
      {/* Header */}
      <div className="chatbot-header">
        <div className="header-left">
          <Bot size={18} className="bot-icon" />
          <span className="header-title">NeuroX Research Agent</span>
        </div>
        <div className="window-dots">
          <div className="dot red"></div>
          <div className="dot yellow"></div>
        </div>
      </div>

      {/* Chat Area */}
      <div className="chat-messages">
        {messages.map((msg, i) => (
          <div key={i} className="message user-message">
            <span className="message-text">{msg.content}</span>
            <User size={14} className="msg-icon user-icon" />
          </div>
        ))}

        {step === "processing" && (
          <div className="message ai-message processing">
            <Sparkles size={14} className="msg-icon ai-icon spin" />
            <span className="thinking-dots">
              Scanning 14,000 market sources...
            </span>
          </div>
        )}

        {(step === "responding" || step === "finished") && (
          <div className="message ai-message">
            <Bot size={14} className="msg-icon ai-icon" />
            {/* Added a distinct style for the research output */}
            <span className="message-text research-output">
              {responseBuffer}
            </span>
          </div>
        )}
      </div>

      {/* Input Area */}
      <div className="chat-input-area">
        <div className="fake-input">
          {inputValue}
          <span className="cursor-blink">|</span>
        </div>
        <div className={`send-btn ${inputValue ? "active" : ""}`}>
          <Send size={16} />
        </div>
      </div>
    </div>
  );
}
