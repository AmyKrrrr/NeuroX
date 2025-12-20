import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./Hero.css";
import HeroChatbot from "./HeroChatbot";

const Typewriter = ({ words, wait = 3000 }) => {
  const [index, setIndex] = useState(0);
  const [subIndex, setSubIndex] = useState(0);
  const [reverse, setReverse] = useState(false);
  const [blink, setBlink] = useState(true);

  useEffect(() => {
    const timeout2 = setTimeout(() => {
      setBlink((prev) => !prev);
    }, 500);
    return () => clearTimeout(timeout2);
  }, [blink]);

  useEffect(() => {
    if (index >= words.length) {
      setIndex(0);
      return;
    }
    if (subIndex === words[index].length + 1 && !reverse) {
      setReverse(true);
      return;
    }
    if (subIndex === 0 && reverse) {
      setReverse(false);
      setIndex((prev) => (prev + 1) % words.length);
      return;
    }
    const timeout = setTimeout(
      () => {
        setSubIndex((prev) => prev + (reverse ? -1 : 1));
      },
      reverse ? 75 : subIndex === words[index].length ? wait : 150
    );
    return () => clearTimeout(timeout);
  }, [subIndex, index, reverse, words, wait]);

  return (
    <span>
      {`${words[index].substring(0, subIndex)}`}
      <span className={`cursor ${blink ? "blink" : ""}`}>|</span>
    </span>
  );
};

export default function Hero() {
  const navigate = useNavigate();

  return (
    <section className="section hero-section">
      <div className="hero-split">
        <div className="hero-left">
          <div className="dashed-pill">NeuroX</div>
          <h1 className="hero-title">
            Built for unbiased <br />
            <span className="highlight-text">
              <Typewriter
                words={[
                  "research",
                  "analysis",
                  "evidence",
                  "verification",
                  "synthesis",
                ]}
                wait={2000}
              />
            </span>
          </h1>
          <p className="hero-subtitle">
            A multi-agent research model that scans sources, cross-verifies
            facts, detects bias, and delivers structured insights without
            repetitive prompting.
          </p>

          <button className="cta-button" onClick={() => navigate("/chatbot")}>
            Get Started
          </button>
        </div>

        <div className="hero-right">
          <HeroChatbot />
        </div>
      </div>
    </section>
  );
}
