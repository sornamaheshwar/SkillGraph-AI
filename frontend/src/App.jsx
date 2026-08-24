import { useCallback, useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

import Profile from "./components/Profile";
import SkillGap from "./components/SkillGap";
import LearningPaths from "./components/LearningPaths";
import Projects from "./components/Projects";
import ProjectDetails from "./components/ProjectDetails";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

function App() {
  const [dashboard, setDashboard] = useState(null);
  const [skillGap, setSkillGap] = useState([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [activePage, setActivePage] = useState("dashboard");
  const [selectedProjectId, setSelectedProjectId] = useState(null);

  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  // ============================================================
  // FETCH DASHBOARD + SKILL GAP DATA
  // ============================================================

  const fetchDashboardData = useCallback(async () => {
    try {
      setError("");

      const [dashboardResponse, skillGapResponse] = await Promise.all([
        axios.get(`${API_BASE_URL}/api/dashboard/`),
        axios.get(`${API_BASE_URL}/api/skills/gap`),
      ]);

      setDashboard(dashboardResponse.data);
      setSkillGap(skillGapResponse.data);
    } catch (err) {
      console.error("Failed to fetch SkillGraph AI data:", err);

      setError(
        "Unable to connect to SkillGraph AI. Please make sure the backend server is running."
      );
    }
  }, []);

  // ============================================================
  // INITIAL LOAD
  // ============================================================

  useEffect(() => {
    const loadInitialData = async () => {
      try {
        setLoading(true);
        await fetchDashboardData();
      } finally {
        setLoading(false);
      }
    };

    loadInitialData();
  }, [fetchDashboardData]);

  // ============================================================
  // PROJECT HANDLERS
  // ============================================================

  const handleSelectProject = (projectId) => {
    setSelectedProjectId(projectId);
    setActivePage("project-details");
  };

  const handleBackToProjects = () => {
    setSelectedProjectId(null);
    setActivePage("projects");
  };

  // ============================================================
  // NAVIGATION
  // ============================================================

  const handleNavigation = (page) => {
    setSelectedProjectId(null);
    setActivePage(page);
    setMobileMenuOpen(false);
  };

  // ============================================================
  // DASHBOARD CALCULATIONS
  // ============================================================

  const acquiredPercentage =
    dashboard?.total_required_skills > 0
      ? Math.round(
          (dashboard.acquired_skills /
            dashboard.total_required_skills) *
            100
        )
      : 0;

  const missingPercentage =
    dashboard?.total_required_skills > 0
      ? Math.round(
          (dashboard.missing_skills /
            dashboard.total_required_skills) *
            100
        )
      : 0;

  // ============================================================
  // LOADING STATE
  // ============================================================

  if (loading) {
    return (
      <div className="app-state">
        <div className="loader"></div>
        <p>Analyzing your skill graph...</p>
      </div>
    );
  }

  // ============================================================
  // ERROR STATE
  // ============================================================

  if (error) {
    return (
      <div className="app-state">
        <h2>Connection Error</h2>

        <p>{error}</p>

        <p className="error-hint">
          Start the FastAPI backend and refresh this page.
        </p>
      </div>
    );
  }

  return (
    <div className="app">
      {/* ================= MOBILE MENU ================= */}

      <button
        className="mobile-menu-button"
        onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
        aria-label="Toggle navigation menu"
      >
        {mobileMenuOpen ? "✕" : "☰"}
      </button>

      {mobileMenuOpen && (
        <div
          className="sidebar-overlay"
          onClick={() => setMobileMenuOpen(false)}
        />
      )}

      {/* ================= SIDEBAR ================= */}

      <aside
        className={`sidebar ${
          mobileMenuOpen ? "mobile-open" : ""
        }`}
      >
        <div className="logo">
          <div className="logo-icon">S</div>
          <span>SkillGraph</span>
        </div>

        <nav className="nav-menu">
          <button
            className={`nav-item ${
              activePage === "dashboard" ? "active" : ""
            }`}
            onClick={() => handleNavigation("dashboard")}
          >
            <span>▦</span>
            Dashboard
          </button>

          <button
            className={`nav-item ${
              activePage === "profile" ? "active" : ""
            }`}
            onClick={() => handleNavigation("profile")}
          >
            <span>◉</span>
            Profile
          </button>

          <button
            className={`nav-item ${
              activePage === "skill-gap" ? "active" : ""
            }`}
            onClick={() => handleNavigation("skill-gap")}
          >
            <span>◈</span>
            Skill Gap
          </button>

          <button
            className={`nav-item ${
              activePage === "learning-paths" ? "active" : ""
            }`}
            onClick={() => handleNavigation("learning-paths")}
          >
            <span>↗</span>
            Learning Paths
          </button>

          <button
            className={`nav-item ${
              activePage === "projects" ||
              activePage === "project-details"
                ? "active"
                : ""
            }`}
            onClick={() => handleNavigation("projects")}
          >
            <span>✦</span>
            Projects
          </button>
        </nav>

        {/* ================= SIDEBAR FOOTER ================= */}

        <div className="sidebar-footer">
          <div className="user-avatar">
            {dashboard?.user_name
              ? dashboard.user_name
                  .split(" ")
                  .map((name) => name[0])
                  .join("")
                  .slice(0, 2)
                  .toUpperCase()
              : "DU"}
          </div>

          <div>
            <p>{dashboard?.user_name || "Demo User"}</p>
            <span>Career Explorer</span>
          </div>
        </div>
      </aside>

      {/* ================= MAIN CONTENT ================= */}

      <main className="main-content">

        {activePage === "dashboard" && (
          <>
            <header className="topbar">
              <div>
                <p className="eyebrow">
                  CAREER INTELLIGENCE
                </p>

                <h1>Your Skill Graph</h1>
              </div>

              <div className="status">
                <span className="status-dot"></span>
                Graph Connected
              </div>
            </header>

            <section className="hero-card">
              <div>
                <p className="eyebrow">
                  TARGET ROLE
                </p>

                <h2>{dashboard?.target_role}</h2>

                <p className="hero-description">
                  Explore your current capabilities, identify missing skills,
                  and discover the best path toward your target role.
                </p>
              </div>

              <div className="readiness-container">
                <div
                  className="readiness-circle"
                  style={{
                    background: `conic-gradient(
                      #ffffff ${dashboard?.readiness_score ?? 0}%,
                      rgba(255, 255, 255, 0.18) 0
                    )`,
                  }}
                >
                  <div className="readiness-inner">
                    <span>
                      {dashboard?.readiness_score ?? 0}%
                    </span>
                  </div>
                </div>

                <p>Role Readiness</p>
              </div>
            </section>

            <section className="stats-grid">
              <div className="stat-card">
                <p>Total Required Skills</p>
                <h3>{dashboard?.total_required_skills ?? 0}</h3>
              </div>

              <div className="stat-card">
                <p>Skills Acquired</p>
                <h3>{dashboard?.acquired_skills ?? 0}</h3>
              </div>

              <div className="stat-card highlight-card">
                <p>Skills To Learn</p>
                <h3>{dashboard?.missing_skills ?? 0}</h3>
              </div>
            </section>

            <section className="skill-progress-card">
              <div className="progress-header">
                <div>
                  <p className="eyebrow">
                    SKILL DISTRIBUTION
                  </p>

                  <h2>Your Current Progress</h2>
                </div>

                <span className="progress-percentage">
                  {acquiredPercentage}% complete
                </span>
              </div>

              <div className="progress-bar">
                <div
                  className="progress-acquired"
                  style={{
                    width: `${acquiredPercentage}%`,
                  }}
                ></div>
              </div>

              <div className="progress-legend">
                <div>
                  <span className="legend-dot acquired"></span>
                  Acquired Skills
                  <strong>
                    {dashboard?.acquired_skills ?? 0}
                  </strong>
                </div>

                <div>
                  <span className="legend-dot missing"></span>
                  Skills Remaining
                  <strong>
                    {dashboard?.missing_skills ?? 0}
                  </strong>
                </div>

                <span className="remaining-percentage">
                  {missingPercentage}% remaining
                </span>
              </div>
            </section>

            <section className="section-header">
              <div>
                <p className="eyebrow">
                  SKILL GAP ANALYSIS
                </p>

                <h2>What to learn next</h2>
              </div>

              <span className="section-count">
                {skillGap.length} skills identified
              </span>
            </section>

            {skillGap.length === 0 ? (
              <div className="empty-state">
                <h3>No skill gaps found 🎉</h3>

                <p>
                  You currently meet all the required skills
                  for this role.
                </p>
              </div>
            ) : (
              <section className="skills-grid">
                {skillGap.map((skill) => (
                  <div
                    className="skill-card"
                    key={skill.id}
                  >
                    <div className="skill-card-top">
                      <span
                        className={`importance ${skill.importance.toLowerCase()}`}
                      >
                        {skill.importance}
                      </span>

                      <span className="weight">
                        Weight {skill.weight}
                      </span>
                    </div>

                    <h3>{skill.name}</h3>

                    <div className="skill-footer">
                      <span>Missing from profile</span>

                      <span className="arrow">→</span>
                    </div>
                  </div>
                ))}
              </section>
            )}
          </>
        )}

        {activePage === "profile" && (
          <Profile
            onProfileUpdate={fetchDashboardData}
          />
        )}

        {activePage === "skill-gap" && <SkillGap />}

        {activePage === "learning-paths" && (
          <LearningPaths />
        )}

        {activePage === "projects" && (
          <Projects
            onSelectProject={handleSelectProject}
          />
        )}

        {activePage === "project-details" &&
          selectedProjectId && (
            <ProjectDetails
              projectId={selectedProjectId}
              onBack={handleBackToProjects}
            />
          )}
      </main>
    </div>
  );
}

export default App;