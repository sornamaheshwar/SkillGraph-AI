import { useEffect, useState } from "react";

const API_BASE_URL = "http://127.0.0.1:8000";

function LearningPaths() {
  const [learningPaths, setLearningPaths] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchLearningPaths = async () => {
      try {
        setLoading(true);
        setError("");

        const response = await fetch(
          `${API_BASE_URL}/api/learning-paths/`
        );

        if (!response.ok) {
          throw new Error("Failed to fetch learning paths");
        }

        const data = await response.json();
        setLearningPaths(data);
      } catch (err) {
        console.error("Failed to fetch learning paths:", err);

        setError(
          "Unable to load learning paths. Please make sure the backend is running."
        );
      } finally {
        setLoading(false);
      }
    };

    fetchLearningPaths();
  }, []);

  if (loading) {
    return (
      <div className="page-state">
        <div className="loader"></div>
        <p>Finding paths through your skill graph...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="page-state error">
        <h3>Unable to load learning paths</h3>
        <p>{error}</p>
      </div>
    );
  }

  return (
    <section className="page-content">
      <div className="page-header">
        <div>
          <p className="eyebrow">LEARNING ROADMAP</p>

          <h1>Your Learning Paths</h1>

          <p className="page-description">
            Discover multi-hop paths through the skill graph that connect
            your current knowledge to Retrieval-Augmented Generation.
          </p>
        </div>

        <div className="page-count">
          {learningPaths.length} paths found
        </div>
      </div>

      {learningPaths.length === 0 ? (
        <div className="empty-state">
          <h3>No learning paths found</h3>

          <p>
            We couldn't find a learning path based on your current skill graph.
          </p>
        </div>
      ) : (
        <div className="learning-paths-grid">
          {learningPaths.map((item, index) => (
            <div
              className="learning-path-card"
              key={`${item.path.join("-")}-${index}`}
            >
              <div className="path-card-header">
                <span className="path-number">
                  Path {index + 1}
                </span>

                <span className="hops-badge">
                  {item.hops} hops
                </span>
              </div>

              <div className="path-skills">
                {item.path.map((skill, skillIndex) => (
                  <div
                    className="path-node-wrapper"
                    key={`${skill}-${skillIndex}`}
                  >
                    <div className="path-node">
                      {skill}
                    </div>

                    {skillIndex < item.path.length - 1 && (
                      <div className="path-arrow">
                        →
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      )}
    </section>
  );
}

export default LearningPaths;