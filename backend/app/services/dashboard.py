from fastapi import HTTPException

from backend.app.core.database import db
from backend.app.queries.dashboard import (
    REQUIRED_SKILLS_QUERY,
    USER_SKILLS_QUERY,
)
from backend.app.schemas.dashboard import DashboardSummary


def get_dashboard_summary(
    user_id: str = "demo-user",
) -> DashboardSummary:
    try:
        with db.get_session() as session:

            # Get all skills required for the target role
            required_result = session.run(
                REQUIRED_SKILLS_QUERY,
                user_id=user_id
            )

            required_skills = [
                dict(record)
                for record in required_result
            ]

            if not required_skills:
                raise HTTPException(
                    status_code=404,
                    detail="User or target role not found."
                )

            # Get skills currently possessed by the user
            user_result = session.run(
                USER_SKILLS_QUERY,
                user_id=user_id
            )

            user_skill_ids = {
                record["skill_id"]
                for record in user_result
            }

        # User and target role information
        user_name = required_skills[0]["user_name"]
        target_role = required_skills[0]["target_role"]

        # Total required skills
        total_required_skills = len(required_skills)

        # Required skills already possessed by the user
        acquired_required_skills = [
            skill
            for skill in required_skills
            if skill["skill_id"] in user_skill_ids
        ]

        acquired_skills = len(acquired_required_skills)

        missing_skills = (
            total_required_skills - acquired_skills
        )

        # Calculate weighted readiness score
        total_weight = sum(
            float(skill["weight"] or 0)
            for skill in required_skills
        )

        acquired_weight = sum(
            float(skill["weight"] or 0)
            for skill in acquired_required_skills
        )

        readiness_score = (
            round(
                (acquired_weight / total_weight) * 100
            )
            if total_weight > 0
            else 0
        )

        return DashboardSummary(
            user_name=user_name,
            target_role=target_role,
            total_required_skills=total_required_skills,
            acquired_skills=acquired_skills,
            missing_skills=missing_skills,
            readiness_score=float(readiness_score),
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database unavailable: {str(e)}"
        )