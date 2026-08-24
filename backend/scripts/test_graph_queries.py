import sys
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BACKEND_DIR))

from app.core.database import db


# ============================================================
# SKILL GAP ANALYSIS
# ============================================================

def test_skill_gap(session):
    # Get all skills required for the user's target role
    query = """
    MATCH (u:User {id: $user_id})-[:TARGETS]->(role:JobRole)
    MATCH (role)-[req:REQUIRES]->(skill:Skill)

    RETURN
        skill.id AS skill_id,
        skill.name AS skill,
        req.importance AS importance,
        req.weight AS weight

    ORDER BY req.weight DESC, skill.name
    """

    result = session.run(query, user_id="demo-user")
    required_skills = [dict(record) for record in result]

    # Get all skills the user already has
    user_query = """
    MATCH (u:User {id: $user_id})-[:HAS_SKILL]->(skill:Skill)

    RETURN skill.id AS skill_id
    """

    user_result = session.run(
        user_query,
        user_id="demo-user"
    )

    user_skill_ids = {
        record["skill_id"]
        for record in user_result
    }

    # Find required skills the user does not have
    missing_skills = [
        skill
        for skill in required_skills
        if skill["skill_id"] not in user_skill_ids
    ]

    print("\n========== SKILL GAP ANALYSIS ==========\n")

    if not missing_skills:
        print("No skill gaps found. You already have all required skills!")

    for skill in missing_skills:
        print(
            f"{skill['skill']} "
            f"| {skill['importance']} "
            f"| weight: {skill['weight']}"
        )


# ============================================================
# MULTI-HOP LEARNING PATH
# ============================================================

def test_learning_path(session):
    query = """
    MATCH (u:User {id: $user_id})-[:HAS_SKILL]->(current:Skill)

    MATCH path =
        (current)-[:PREREQUISITE_OF*1..5]->(
            target:Skill {id: $target_skill_id}
        )

    RETURN
        [node IN nodes(path) | node.name] AS learning_path,
        length(path) AS path_length

    ORDER BY path_length ASC
    LIMIT 5
    """

    result = session.run(
        query,
        user_id="demo-user",
        target_skill_id="rag"
    )

    print("\n========== MULTI-HOP LEARNING PATH ==========\n")

    found = False

    for record in result:
        found = True

        path = " → ".join(record["learning_path"])

        print(
            f"{path} "
            f"(hops: {record['path_length']})"
        )

    if not found:
        print("No learning path found.")


# ============================================================
# PROJECT RECOMMENDATIONS
# ============================================================

def test_project_recommendations(session):
    # Find projects relevant to the user's target role
    projects_query = """
    MATCH (u:User {id: $user_id})-[:TARGETS]->(role:JobRole)

    MATCH (project:Project)-[:RELEVANT_TO]->(role)

    MATCH (project)-[:DEMONSTRATES]->(skill:Skill)

    RETURN
        project.name AS project,
        project.id AS project_id,
        COLLECT(skill.id) AS skill_ids,
        COLLECT(skill.name) AS skill_names
    """

    result = session.run(
        projects_query,
        user_id="demo-user"
    )

    projects = [dict(record) for record in result]

    # Get the skills the user already has
    user_query = """
    MATCH (u:User {id: $user_id})-[:HAS_SKILL]->(skill:Skill)

    RETURN skill.id AS skill_id
    """

    user_result = session.run(
        user_query,
        user_id="demo-user"
    )

    user_skill_ids = {
        record["skill_id"]
        for record in user_result
    }

    recommendations = []

    # Find which missing skills each project can help demonstrate
    for project in projects:

        missing_skills = [
            skill_name
            for skill_id, skill_name in zip(
                project["skill_ids"],
                project["skill_names"]
            )
            if skill_id not in user_skill_ids
        ]

        if missing_skills:
            recommendations.append(
                {
                    "project": project["project"],
                    "missing_skills_covered": missing_skills,
                    "relevance_score": len(missing_skills),
                }
            )

    # Sort projects by number of missing skills covered
    recommendations.sort(
        key=lambda x: x["relevance_score"],
        reverse=True
    )

    print("\n========== PROJECT RECOMMENDATIONS ==========\n")

    if not recommendations:
        print("No project recommendations found.")
        return

    for project in recommendations[:5]:

        skills = ", ".join(
            project["missing_skills_covered"]
        )

        print(project["project"])
        print(f"  Covers: {skills}")
        print(
            f"  Score: {project['relevance_score']}\n"
        )


# ============================================================
# MAIN
# ============================================================

def main():
    try:
        print("Connecting to CognoDB...")

        db.verify_connection()

        with db.get_session() as session:
            test_skill_gap(session)
            test_learning_path(session)
            test_project_recommendations(session)

    except Exception as e:
        print(f"\nQuery test failed: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    main()