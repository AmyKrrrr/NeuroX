import React, { useState, useEffect } from "react";
import "./App.css";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useNavigate,
  useLocation,
} from "react-router-dom";

// Components
import LandingPage from "./components/LandingPage";
import FullPageChatbot from "./components/FullPageChatbot";
import { Home, Code2, Users, MessageSquare } from "lucide-react";

// --- NAV BAR COMPONENT ---
// We extract Navbar so it can use routing hooks (useLocation, useNavigate)
const Navbar = () => {
  const [activeSection, setActiveSection] = useState("hero");
  const navigate = useNavigate();
  const location = useLocation();
  const isChatbotPage = location.pathname === "/chatbot";

  // Scroll Spy Logic (Only runs on Home Page)
  useEffect(() => {
    if (isChatbotPage) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) setActiveSection(entry.target.id);
        });
      },
      { rootMargin: "-45% 0px -45% 0px", threshold: 0 }
    );

    const sections = document.querySelectorAll("div[id]");
    sections.forEach((s) => observer.observe(s));
    return () => sections.forEach((s) => observer.unobserve(s));
  }, [isChatbotPage]);

  // Handle Navigation Clicks
  const handleNavClick = (sectionId) => {
    if (isChatbotPage) {
      // If on chatbot page, go Home first, then scroll
      navigate("/");
      setTimeout(() => {
        document
          .getElementById(sectionId)
          ?.scrollIntoView({ behavior: "smooth" });
      }, 100);
    } else {
      // If already on Home, just scroll
      document
        .getElementById(sectionId)
        ?.scrollIntoView({ behavior: "smooth" });
    }
  };

  const getNavClass = (id) => {
    // If we are on chatbot page, only highlight the chat icon
    if (isChatbotPage) return id === "chat" ? "nav-item active" : "nav-item";
    // Otherwise use scroll-spy active state
    return `nav-item ${activeSection === id ? "active" : ""}`;
  };

  return (
    <nav className="floating-nav">
      <div
        className={getNavClass("hero")}
        onClick={() => handleNavClick("hero")}
      >
        <Home size={20} />
      </div>
      <div
        className={getNavClass("code")}
        onClick={() => handleNavClick("code")}
      >
        <Code2 size={20} />
      </div>
      <div
        className={getNavClass("team")}
        onClick={() => handleNavClick("team")}
      >
        <Users size={20} />
      </div>
      {/* 4th Icon: Navigates to /chatbot */}
      <div className={getNavClass("chat")} onClick={() => navigate("/chatbot")}>
        <MessageSquare size={20} />
      </div>
    </nav>
  );
};

// --- MAIN APP COMPONENT ---
function App() {
  return (
    <Router>
      <div className="app-container">
        {/* Navbar is outside Routes so it stays visible on both pages */}
        <Navbar />

        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/chatbot" element={<FullPageChatbot />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
