import { useEffect, useState } from "react";
import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

function ProjectDetails({ projectId, onBack }) {
  const [project, setProject] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchProjectDetails = async () => {
      try {
        setLoading(true);
        setError("");

        const response = await axios.get(
          `${API_BASE_URL}/api/projects/${projectId}`
        );

        setProject(response.data);
      } catch (err) {
        console.error(
          "Failed to fetch project details:",
          err
        );

        setError(
          "Unable to load project details. Please try again."
        );
      } finally {
        setLoading(false);
      }
    };

    if (projectId) {
      fetchProjectDetails();
    }
  }, [projectId]);

  if (loading) {
    return (
      <div className="page-state">
        <div className="loader"></div>

        <p>Building your project roadmap...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="page-state">
        <h2>Unable to load project details</h2>

        <p>{error}</p>

        <button
          className="back-button"
          onClick={onBack}
        >
          ← Back to Projects
        </button>
      </div>
    );
  }

  if (!project) {
    return null;
  }

  return (
    <div className="project-details-page">

      {/* ================= BACK BUTTON ================= */}

      <button
        className="back-button"
        onClick={onBack}
      >
        ← Back to Projects
      </button>

      {/* ================= PROJECT HERO ================= */}

      <section className="project-details-hero">
        <div>
          <p className="eyebrow">
            PROJECT ROADMAP
          </p>

          <h1>{project.name}</h1>

          <p className="project-details-description">
            {project.description}
          </p>
        </div>

        <div className="project-details-meta">
          <span
            className={`difficulty ${project.difficulty.toLowerCase()}`}
          >
            {project.difficulty}
          </span>

          <span className="project-skills-count">
            {project.skills.length} skills covered
          </span>
        </div>
      </section>

      {/* ================= SKILLS ================= */}

      <section className="details-section">
        <p className="eyebrow">
          SKILLS
        </p>

        <h2>Skills You Will Demonstrate</h2>

        <div className="skill-tags details-tags">
          {project.skills.map((skill) => (
            <span
              className="skill-tag"
              key={skill}
            >
              {skill}
            </span>
          ))}
        </div>
      </section>

      {/* ================= TECH STACK ================= */}

      <section className="details-section">
        <p className="eyebrow">
          TECHNOLOGY STACK
        </p>

        <h2>Recommended Tools</h2>

        <div className="tech-stack-grid">
          {project.tech_stack.map((tech) => (
            <div
              className="tech-item"
              key={tech}
            >
              {tech}
            </div>
          ))}
        </div>
      </section>

      {/* ================= FEATURES ================= */}

      <section className="details-section">
        <p className="eyebrow">
          CORE FEATURES
        </p>

        <h2>What You Should Build</h2>

        <div className="features-grid">
          {project.key_features.map((feature) => (
            <div
              className="feature-item"
              key={feature}
            >
              <span className="feature-icon">
                ✓
              </span>

              <span>{feature}</span>
            </div>
          ))}
        </div>
      </section>

      {/* ================= ARCHITECTURE ================= */}

      <section className="details-section">
        <p className="eyebrow">
          SYSTEM ARCHITECTURE
        </p>

        <h2>Application Flow</h2>

        <div className="architecture-flow">
          {project.architecture.map(
            (step, index) => (
              <div
                className="architecture-step"
                key={`${step}-${index}`}
              >
                <div className="architecture-number">
                  {index + 1}
                </div>

                <span>{step}</span>

                {index <
                  project.architecture.length - 1 && (
                  <div className="architecture-arrow">
                    ↓
                  </div>
                )}
              </div>
            )
          )}
        </div>
      </section>

      {/* ================= IMPLEMENTATION ROADMAP ================= */}

      <section className="details-section roadmap-section">
        <p className="eyebrow">
          IMPLEMENTATION ROADMAP
        </p>

        <h2>Build It Step by Step</h2>

        <div className="roadmap-list">
          {project.implementation_steps.map(
            (item) => (
              <div
                className="roadmap-item"
                key={item.step}
              >
                <div className="roadmap-number">
                  {item.step}
                </div>

                <div className="roadmap-content">
                  <h3>{item.title}</h3>

                  <p>
                    {item.description}
                  </p>
                </div>
              </div>
            )
          )}
        </div>
      </section>

    </div>
  );
}

export default ProjectDetails;