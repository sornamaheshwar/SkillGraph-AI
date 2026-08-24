from fastapi import APIRouter, HTTPException

from backend.app.core.database import db
from backend.app.schemas.learning_path import LearningPath


router = APIRouter(
    prefix="/api/learning-paths",
    tags=["Learning Paths"]
)


@router.get("/", response_model=list[LearningPath])
def get_learning_paths():
    query = """
    MATCH (u:User {id: $user_id})-[:HAS_SKILL]->(current:Skill)

    MATCH path =
        (current)-[:PREREQUISITE_OF*1..5]->(
            target:Skill {id: $target_skill_id}
        )

    RETURN
        [node IN nodes(path) | node.name] AS path,
        length(path) AS hops

    ORDER BY hops ASC
    LIMIT 5
    """

    try:
        with db.get_session() as session:

            result = session.run(
                query,
                user_id="demo-user",
                target_skill_id="rag"
            )

            learning_paths = [
                LearningPath(
                    path=record["path"],
                    hops=record["hops"]
                )
                for record in result
            ]

        return learning_paths

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database unavailable: {str(e)}"
        )