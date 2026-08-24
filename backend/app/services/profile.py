from fastapi import HTTPException

from backend.app.core.database import db
from backend.app.schemas.profile import Profile


def get_user_profile(
    user_id: str = "demo-user",
) -> Profile:
    query = """
    MATCH (u:User {id: $user_id})

    OPTIONAL MATCH (u)-[:TARGETS]->(role:JobRole)

    OPTIONAL MATCH (u)-[:HAS_SKILL]->(skill:Skill)

    RETURN
        u.id AS user_id,
        u.name AS user_name,
        role.name AS target_role,
        collect(skill.name) AS skills
    """

    try:
        with db.get_session() as session:
            result = session.run(
                query,
                user_id=user_id
            )

            record = result.single()

            if record is None:
                raise HTTPException(
                    status_code=404,
                    detail="User not found."
                )

            return Profile(
                user_id=record["user_id"],
                user_name=record["user_name"],
                target_role=record["target_role"],
                skills=record["skills"]
            )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database unavailable: {str(e)}"
        )