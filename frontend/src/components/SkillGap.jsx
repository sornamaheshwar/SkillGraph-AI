import { useEffect, useState } from "react";

const API_BASE_URL = "http://127.0.0.1:8000";

function SkillGap() {
  const [skills, setSkills] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchSkillGap = async () => {
      try {
        setLoading(true);
        setError("");

        const response = await fetch(
          `${API_BASE_URL}/api/skills/gap`
        );

        if (!response.ok) {
          throw new Error("Failed to fetch skill gap");
        }

        const data = await response.json();

        setSkills(data);
      } catch (err) {
        console.error(
          "Failed to fetch skill gap:",
          err
        );

        setError(
          "Unable to load skill gap data. Please make sure the backend is running."
        );
      } finally {
        setLoading(false);
      }
    };

    fetchSkillGap();
  }, []);

  if (loading) {
    return (
      <div className="page-state">
        <div className="loader"></div>

        <p>Analyzing your skill gaps...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="page-state error">
        <h2>Unable to load skill gap analysis</h2>

        <p>{error}</p>
      </div>
    );
  }

  return (
    <div className="page-container">
      {/* ================= PAGE HEADER ================= */}

      <div className="page-header">
        <div>
          <p className="eyebrow">
            SKILL GAP ANALYSIS
          </p>

          <h1>Your Missing Skills</h1>

          <p className="page-description">
            Focus on these skills to move closer to your
            target role.
          </p>
        </div>

        <div className="skill-count">
          {skills.length} skill
          {skills.length !== 1 ? "s" : ""} identified
        </div>
      </div>

      {/* ================= EMPTY STATE ================= */}

      {skills.length === 0 ? (
        <div className="empty-state">
          <h3>No skill gaps found 🎉</h3>

          <p>
            You currently meet all the required skills
            for your target role.
          </p>
        </div>
      ) : (
        /* ================= SKILL CARDS ================= */

        <div className="skills-grid">
          {skills.map((skill) => {
            const priorityWidth = Math.min(
              skill.weight * 10,
              100
            );

            const priorityLabel =
              skill.weight >= 10
                ? "High Priority"
                : skill.weight >= 7
                  ? "Medium Priority"
                  : "Supporting Skill";

            return (
              <div
                className="skill-card"
                key={skill.id}
              >
                <div className="skill-card-header">
                  <span
                    className={`importance-badge ${skill.importance.toLowerCase()}`}
                  >
                    {skill.importance}
                  </span>

                  <span className="weight">
                    Weight {skill.weight}
                  </span>
                </div>

                <h3>{skill.name}</h3>

                {/* ================= PRIORITY ================= */}

                <div className="priority-section">
                  <span>Learning Priority</span>

                  <div className="priority-bar">
                    <div
                      className="priority-fill"
                      style={{
                        width: `${priorityWidth}%`,
                      }}
                    />
                  </div>
                </div>

                <div className="priority-label">
                  {priorityLabel}
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

export default SkillGap;