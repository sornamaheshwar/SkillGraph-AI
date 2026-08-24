import { useEffect, useState } from "react";
import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

function Projects({ onSelectProject }) {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        setLoading(true);
        setError("");

        const response = await axios.get(
          `${API_BASE_URL}/api/projects/recommendations`
        );

        setProjects(response.data);
      } catch (err) {
        console.error(
          "Failed to fetch project recommendations:",
          err
        );

        setError(
          "Unable to load project recommendations."
        );
      } finally {
        setLoading(false);
      }
    };

    fetchProjects();
  }, []);

  if (loading) {
    return (
      <div className="page-state">
        <div className="loader"></div>

        <p>
          Finding the best projects for your skill gaps...
        </p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="page-state">
        <h2>Unable to load projects</h2>

        <p>{error}</p>
      </div>
    );
  }

  return (
    <div className="projects-page">

      {/* ================= PAGE HEADER ================= */}

      <header className="page-header projects-header">
        <div>
          <p className="eyebrow">
            PROJECT RECOMMENDATIONS
          </p>

          <h1>Build Your Next Project</h1>

          <p className="page-description">
            Recommended projects based on the skills you
            still need for your target role.
          </p>
        </div>

        <div className="section-count">
          {projects.length} project
          {projects.length !== 1 ? "s" : ""} found
        </div>
      </header>

      {/* ================= PROJECT RECOMMENDATION INTRO ================= */}

      <section className="projects-recommendation-section">

        <div className="projects-section-heading">
          <div>
            <p className="eyebrow">
              MATCHED TO YOUR SKILL GAPS
            </p>

            <h2>
              Projects you should build next
            </h2>
          </div>

          <p>
            Ranked by how many missing skills each project
            helps you demonstrate.
          </p>
        </div>

        {/* ================= EMPTY STATE ================= */}

        {projects.length === 0 ? (
          <div className="empty-state">
            <h3>
              No project recommendations found 🎉
            </h3>

            <p>
              You currently don't have any skill gaps that
              require project recommendations.
            </p>
          </div>
        ) : (
          /* ================= PROJECT CARDS ================= */

          <section className="projects-grid">
            {projects.map((project) => (
              <button
                type="button"
                className="project-card project-card-button"
                key={project.id}
                onClick={() =>
                  onSelectProject(project.id)
                }
              >
                <div className="project-card-header">
                  <span
                    className={`difficulty ${project.difficulty.toLowerCase()}`}
                  >
                    {project.difficulty}
                  </span>

                  <span className="relevance-score">
                    Covers {project.relevance_score} skill
                    {project.relevance_score !== 1
                      ? "s"
                      : ""}
                  </span>
                </div>

                <h2>{project.name}</h2>

                <p className="project-description">
                  {project.description}
                </p>

                <div className="project-skills">
                  <p>
                    Skills you can demonstrate
                  </p>

                  <div className="skill-tags">
                    {project.missing_skills_covered.map(
                      (skill) => (
                        <span
                          className="skill-tag"
                          key={skill}
                        >
                          {skill}
                        </span>
                      )
                    )}
                  </div>
                </div>

                <div className="project-footer">
                  <span>
                    View Implementation Roadmap
                  </span>

                  <span className="arrow">
                    →
                  </span>
                </div>
              </button>
            ))}
          </section>
        )}

      </section>
    </div>
  );
}

export default Projects;