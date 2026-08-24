import sys
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BACKEND_DIR))

from app.core.database import db


def verify_database():
    queries = {
        "Users": "MATCH (n:User) RETURN count(n) AS count",
        "Skills": "MATCH (n:Skill) RETURN count(n) AS count",
        "Job Roles": "MATCH (n:JobRole) RETURN count(n) AS count",
        "Technologies": "MATCH (n:Technology) RETURN count(n) AS count",
        "Projects": "MATCH (n:Project) RETURN count(n) AS count",

        "Prerequisite Relationships":
            "MATCH ()-[r:PREREQUISITE_OF]->() RETURN count(r) AS count",

        "Role Requirements":
            "MATCH ()-[r:REQUIRES]->() RETURN count(r) AS count",

        "User Skills":
            "MATCH ()-[r:HAS_SKILL]->() RETURN count(r) AS count",

        "User Target Roles":
            "MATCH ()-[r:TARGETS]->() RETURN count(r) AS count",

        "Project Skills":
            "MATCH ()-[r:DEMONSTRATES]->() RETURN count(r) AS count",

        "Project Roles":
            "MATCH ()-[r:RELEVANT_TO]->() RETURN count(r) AS count",

        "Skill Technologies":
            "MATCH ()-[r:USES]->() RETURN count(r) AS count",
    }

    try:
        print("\nVerifying SkillGraph AI database...\n")

        db.verify_connection()

        with db.get_session() as session:
            for name, query in queries.items():
                result = session.run(query)
                record = result.single()

                print(f"{name}: {record['count']}")

    except Exception as e:
        print(f"Verification failed: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    verify_database()