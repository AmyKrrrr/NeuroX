import React from "react";
import "./Team.css";

// 1. IMPORT THE IMAGES HERE
// (The names 'subratImg', etc. are variables we create to hold the image data)
import subratImg from "../subrat.jpg";
import mateenImg from "../mateen.jpg";
import amiteshImg from "../amitesh.jpg";

const teamMembers = [
  {
    id: 1,
    name: "Subrat Mishra",
    role: "Backend Engineer",
    // 2. USE THE VARIABLE HERE (No quotes!)
    image: subratImg,
  },
  {
    id: 2,
    name: "Abdul Mateen",
    role: "Orchestration of Agents",
    image: mateenImg,
  },
  {
    id: 3,
    name: "Amitesh Kar",
    role: "Frontend Engineer",
    image: amiteshImg,
  },
];

export default function Team() {
  return (
    <section className="section team-section">
      <div className="team-container">
        <div className="team-header">
          <h2 className="team-title">Our Team</h2>
          <p className="team-subtitle">Developed by</p>
        </div>

        <div className="team-grid">
          {teamMembers.map((member) => (
            <div key={member.id} className="team-card">
              <div className="image-wrapper">
                {/* The src will now correctly point to the bundled image */}
                <img
                  src={member.image}
                  alt={member.name}
                  className="member-image"
                />
              </div>
              <h3 className="member-name">{member.name}</h3>
              <p className="member-role">{member.role}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
