import "./CodeShowcase.css";

import React from "react";
import { Copy } from "lucide-react";
// Adjust path to your image
import keyboardImage from "../keyboard2.webp";

// --- Internal Code Window Component ---
const CodeWindow = () => {
  return (
    <div className="code-window">
      <div className="code-header">
        <div className="window-dots">
          <div className="dot red"></div>
          <div className="dot yellow"></div>
          <div className="dot green"></div>
        </div>
        <div className="window-title">useCardStack.ts</div>
        <Copy size={16} className="copy-icon" />
      </div>
      <div className="code-content">
        <div className="line">
          <span className="keyword">"use client"</span>;
        </div>
        <div className="line">
          <span className="keyword">import</span> {"{"}{" "}
          <span className="function">useEffect</span>,{" "}
          <span className="function">useState</span> {"}"}{" "}
          <span className="keyword">from</span>{" "}
          <span className="string">"react"</span>;
        </div>
        <div className="line">
          <span className="keyword">import</span> {"{"} motion {"}"}{" "}
          <span className="keyword">from</span>{" "}
          <span className="string">"motion/react"</span>;
        </div>
        <br />
        <div className="line">
          <span className="keyword">let</span>{" "}
          <span className="variable">interval</span>:{" "}
          <span className="type">any</span>;
        </div>
        <br />
        <div className="line">
          <span className="keyword">type</span>{" "}
          <span className="type">Card</span> = {"{"}
        </div>
        <div className="line indent">
          <span className="property">id</span>:{" "}
          <span className="type">number</span>;
        </div>
        <div className="line indent">
          <span className="property">name</span>:{" "}
          <span className="type">string</span>;
        </div>
        <div className="line indent">
          <span className="property">designation</span>:{" "}
          <span className="type">string</span>;
        </div>
        <div className="line indent">
          <span className="property">content</span>:{" "}
          <span className="type">React.ReactNode</span>;
        </div>
        <div className="line">{"}"};</div>
        <br />
        <div className="line">
          <span className="keyword">export const</span>{" "}
          <span className="function">CardStack</span> = ({"{"}
        </div>
        <div className="line indent">items, offset, scaleFactor</div>
        <div className="line">
          {"}"}) ={">"} {"{"}
        </div>
        <div className="line indent">
          <span className="keyword">const</span>{" "}
          <span className="variable">CARD_OFFSET</span> = offset ||{" "}
          <span className="number">10</span>;
        </div>
        <div className="line indent">
          <span className="keyword">const</span>{" "}
          <span className="variable">SCALE_FACTOR</span> = scaleFactor ||{" "}
          <span className="number">0.06</span>;
        </div>
        <div className="line indent">
          <span className="keyword">const</span> [cards, setCards] ={" "}
          <span className="function">useState</span>
          {"<"}
          <span className="type">Card</span>[]={">"}(items);
        </div>
        <br />
        <div className="line indent">
          <span className="function">useEffect</span>(() ={">"} {"{"}
        </div>
      </div>
    </div>
  );
};

export default function CodeShowcase() {
  return (
    <section className="section code-section">
      <div className="showcase-wrapper">
        {/* Layer 1: Keyboard (Base) */}
        <div className="keyboard-layer">
          <img
            src={keyboardImage}
            alt="Mechanical Keyboard"
            className="keyboard-img"
          />
        </div>
        {/* Layer 2: Code Window (Floating) */}
        <div className="code-layer">
          <CodeWindow />
        </div>
      </div>
    </section>
  );
}
