import { useEffect, useState } from "react";
import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

function Profile({ onProfileUpdate }) {
  const [profile, setProfile] = useState(null);
  const [availableSkills, setAvailableSkills] = useState([]);
  const [selectedSkillId, setSelectedSkillId] = useState("");

  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);
  const [error, setError] = useState("");

  // ============================================================
  // FETCH PROFILE + AVAILABLE SKILLS
  // ============================================================

  const fetchProfileData = async () => {
    try {
      setLoading(true);
      setError("");

      const [profileResponse, skillsResponse] = await Promise.all([
        axios.get(`${API_BASE_URL}/api/profile/`),
        axios.get(`${API_BASE_URL}/api/skills/`),
      ]);

      setProfile(profileResponse.data);
      setAvailableSkills(skillsResponse.data);
    } catch (err) {
      console.error("Failed to fetch profile data:", err);

      setError(
        "Unable to load your profile. Please make sure the backend is running."
      );
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProfileData();
  }, []);

  // ============================================================
  // ADD SKILL
  // ============================================================

  const handleAddSkill = async () => {
    if (!selectedSkillId) {
      return;
    }

    try {
      setActionLoading(true);

      await axios.post(`${API_BASE_URL}/api/skills/user`, {
        skill_id: selectedSkillId,
      });

      setSelectedSkillId("");

      // Refresh Profile data
      await fetchProfileData();

      // Refresh Dashboard + Skill Gap data in App.jsx
      if (onProfileUpdate) {
        await onProfileUpdate();
      }
    } catch (err) {
      console.error("Failed to add skill:", err);

      alert(
        err.response?.data?.detail ||
          "Unable to add the skill."
      );
    } finally {
      setActionLoading(false);
    }
  };

  // ============================================================
  // REMOVE SKILL
  // ============================================================

  const handleRemoveSkill = async (skillName) => {
    try {
      setActionLoading(true);

      const matchingSkill = availableSkills.find(
        (item) => item.name === skillName
      );

      if (!matchingSkill) {
        alert("Skill ID could not be found.");
        return;
      }

      await axios.delete(
        `${API_BASE_URL}/api/skills/user/${matchingSkill.id}`
      );

      // Refresh Profile data
      await fetchProfileData();

      // Refresh Dashboard + Skill Gap data in App.jsx
      if (onProfileUpdate) {
        await onProfileUpdate();
      }
    } catch (err) {
      console.error("Failed to remove skill:", err);

      alert(
        err.response?.data?.detail ||
          "Unable to remove the skill."
      );
    } finally {
      setActionLoading(false);
    }
  };

  // ============================================================
  // LOADING STATE
  // ============================================================

  if (loading) {
    return (
      <div className="page-state">
        <div className="loader"></div>

        <p>Loading your profile...</p>
      </div>
    );
  }

  // ============================================================
  // ERROR STATE
  // ============================================================

  if (error) {
    return (
      <div className="page-state error">
        <h2>Unable to load profile</h2>

        <p>{error}</p>
      </div>
    );
  }

  if (!profile) {
    return null;
  }

  // ============================================================
  // FILTER SKILLS NOT ALREADY OWNED
  // ============================================================

  const userSkillNames = new Set(profile.skills);

  const skillsToAdd = availableSkills.filter(
    (skill) => !userSkillNames.has(skill.name)
  );

  // ============================================================
  // PROFILE UI
  // ============================================================

  return (
    <div className="profile-page">

      {/* ================= PROFILE HERO ================= */}

      <section className="profile-hero">
        <div className="profile-avatar">
          {profile.user_name
            .split(" ")
            .map((name) => name[0])
            .join("")
            .slice(0, 2)
            .toUpperCase()}
        </div>

        <div className="profile-info">
          <p className="eyebrow">
            CAREER PROFILE
          </p>

          <h1>{profile.user_name}</h1>

          <p className="profile-role">
            Aspiring {profile.target_role}
          </p>
        </div>
      </section>

      {/* ================= PROFILE OVERVIEW ================= */}

      <section className="profile-overview">
        <div className="profile-stat-card">
          <p>Target Role</p>

          <h3>{profile.target_role}</h3>
        </div>

        <div className="profile-stat-card">
          <p>Current Skills</p>

          <h3>{profile.skills.length}</h3>
        </div>

        <div className="profile-stat-card">
          <p>Profile ID</p>

          <h3>{profile.user_id}</h3>
        </div>
      </section>

      {/* ================= ADD SKILL ================= */}

      <section className="add-skill-section">
        <div className="section-header">
          <div>
            <p className="eyebrow">
              UPDATE PROFILE
            </p>

            <h2>Add a Skill</h2>
          </div>
        </div>

        <div className="add-skill-container">
          <select
            value={selectedSkillId}
            onChange={(event) =>
              setSelectedSkillId(event.target.value)
            }
            disabled={actionLoading}
          >
            <option value="">
              Select a skill to add
            </option>

            {skillsToAdd.map((skill) => (
              <option
                key={skill.id}
                value={skill.id}
              >
                {skill.name}
              </option>
            ))}
          </select>

          <button
            className="add-skill-button"
            onClick={handleAddSkill}
            disabled={
              !selectedSkillId ||
              actionLoading
            }
          >
            {actionLoading
              ? "Updating..."
              : "+ Add Skill"}
          </button>
        </div>
      </section>

      {/* ================= CURRENT SKILLS ================= */}

      <section className="profile-skills-section">
        <div className="section-header">
          <div>
            <p className="eyebrow">
              SKILL PROFILE
            </p>

            <h2>Your Current Skills</h2>
          </div>

          <span className="section-count">
            {profile.skills.length} skills
          </span>
        </div>

        {profile.skills.length === 0 ? (
          <div className="empty-state">
            <h3>No skills added yet</h3>

            <p>
              Add your skills to start building your
              career intelligence profile.
            </p>
          </div>
        ) : (
          <div className="profile-skills-grid">
            {profile.skills.map((skill) => (
              <div
                className="profile-skill-card"
                key={skill}
              >
                <div className="profile-skill-content">
                  <div className="profile-skill-icon">
                    ✓
                  </div>

                  <span>{skill}</span>
                </div>

                <button
                  className="remove-skill-button"
                  onClick={() =>
                    handleRemoveSkill(skill)
                  }
                  disabled={actionLoading}
                  title={`Remove ${skill}`}
                >
                  ×
                </button>
              </div>
            ))}
          </div>
        )}
      </section>

    </div>
  );
}

export default Profile;