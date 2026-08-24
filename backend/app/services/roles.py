from fastapi import HTTPException

from backend.app.core.database import db
from backend.app.schemas.role import JobRole
from backend.app.queries.roles import GET_ALL_ROLES


def get_all_roles() -> list[JobRole]:
    try:
        with db.get_session() as session:
            result = session.run(GET_ALL_ROLES)

            roles = [
                JobRole(**dict(record))
                for record in result
            ]

        return roles

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database unavailable: {str(e)}"
        )