import React from "react";
import LiquidEther from "./LiquidEther";
import Hero from "./Hero";
import CodeShowcase from "./CodeShowcase";
import Team from "./Team";

export default function LandingPage() {
  return (
    <>
      {/* BACKGROUND */}
      <div className="fixed-background">
        <LiquidEther
          colors={["#5227FF", "#FF9FFC", "#B19EEF"]}
          mouseForce={20}
          cursorSize={100}
          isViscous={false}
          viscous={30}
          iterationsViscous={32}
          iterationsPoisson={32}
          resolution={0.5}
          isBounce={false}
          autoDemo={true}
          autoSpeed={0.5}
          autoIntensity={2.2}
          takeoverDuration={0.25}
          autoResumeDelay={3000}
          autoRampDuration={0.6}
        />
      </div>

      {/* CONTENT */}
      <div className="scroll-content">
        <div id="hero">
          <Hero />
        </div>
        <div id="code">
          <CodeShowcase />
        </div>
        <div id="team">
          <Team />
        </div>
      </div>
    </>
  );
}
