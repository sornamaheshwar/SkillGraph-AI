from fastapi import APIRouter, HTTPException, status

from backend.app.core.database import db
from backend.app.schemas.skill import (
    Skill,
    SkillGap,
    LearningPath,
    UserSkillRequest,
)


router = APIRouter(
    prefix="/api/skills",
    tags=["Skills"]
)


# ============================================================
# GET ALL AVAILABLE SKILLS
# ============================================================

@router.get("/", response_model=list[Skill])
def get_all_skills():
    query = """
    MATCH (skill:Skill)

    RETURN
        skill.id AS id,
        skill.name AS name,
        skill.category AS category

    ORDER BY skill.name
    """

    try:
        with db.get_session() as session:
            result = session.run(query)

            skills = [
                Skill(**dict(record))
                for record in result
            ]

        return skills

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database unavailable: {str(e)}"
        )


# ============================================================
# GET USER'S CURRENT SKILLS
# ============================================================

@router.get("/user", response_model=list[Skill])
def get_user_skills():
    query = """
    MATCH (u:User {id: $user_id})-[:HAS_SKILL]->(skill:Skill)

    RETURN
        skill.id AS id,
        skill.name AS name,
        skill.category AS category

    ORDER BY skill.name
    """

    try:
        with db.get_session() as session:
            result = session.run(
                query,
                user_id="demo-user"
            )

            skills = [
                Skill(**dict(record))
                for record in result
            ]

        return skills

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database unavailable: {str(e)}"
        )


# ============================================================
# ADD A SKILL TO USER
# ============================================================

@router.post(
    "/user",
    response_model=Skill,
    status_code=status.HTTP_201_CREATED
)
def add_user_skill(skill_request: UserSkillRequest):
    query = """
    MATCH (u:User {id: $user_id})
    MATCH (skill:Skill {id: $skill_id})

    MERGE (u)-[:HAS_SKILL]->(skill)

    RETURN
        skill.id AS id,
        skill.name AS name,
        skill.category AS category
    """

    try:
        with db.get_session() as session:
            result = session.run(
                query,
                user_id="demo-user",
                skill_id=skill_request.skill_id
            )

            record = result.single()

            if record is None:
                raise HTTPException(
                    status_code=404,
                    detail="User or skill not found."
                )

            return Skill(**dict(record))

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database unavailable: {str(e)}"
        )


# ============================================================
# REMOVE A SKILL FROM USER
# ============================================================

@router.delete("/user/{skill_id}")
def remove_user_skill(skill_id: str):
    query = """
    MATCH (u:User {id: $user_id})-[relationship:HAS_SKILL]->(
        skill:Skill {id: $skill_id}
    )

    DELETE relationship

    RETURN skill.id AS id
    """

    try:
        with db.get_session() as session:
            result = session.run(
                query,
                user_id="demo-user",
                skill_id=skill_id
            )

            record = result.single()

            if record is None:
                raise HTTPException(
                    status_code=404,
                    detail="Skill not found in user's profile."
                )

        return {
            "message": "Skill removed successfully.",
            "skill_id": skill_id
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database unavailable: {str(e)}"
        )


# ============================================================
# SKILL GAP ANALYSIS
# ============================================================

@router.get("/gap", response_model=list[SkillGap])
def get_skill_gap():
    required_skills_query = """
    MATCH (u:User {id: $user_id})-[:TARGETS]->(role:JobRole)
    MATCH (role)-[req:REQUIRES]->(skill:Skill)

    RETURN
        skill.id AS id,
        skill.name AS name,
        req.importance AS importance,
        req.weight AS weight

    ORDER BY req.weight DESC, skill.name
    """

    user_skills_query = """
    MATCH (u:User {id: $user_id})-[:HAS_SKILL]->(skill:Skill)

    RETURN skill.id AS id
    """

    try:
        with db.get_session() as session:

            required_result = session.run(
                required_skills_query,
                user_id="demo-user"
            )

            required_skills = [
                dict(record)
                for record in required_result
            ]

            user_result = session.run(
                user_skills_query,
                user_id="demo-user"
            )

            user_skill_ids = {
                record["id"]
                for record in user_result
            }

        missing_skills = [
            SkillGap(**skill)
            for skill in required_skills
            if skill["id"] not in user_skill_ids
        ]

        return missing_skills

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database unavailable: {str(e)}"
        )


# ============================================================
# LEARNING PATHS
# ============================================================

@router.get(
    "/learning-path",
    response_model=list[LearningPath]
)
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

            paths = [
                LearningPath(**dict(record))
                for record in result
            ]

        return paths

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database unavailable: {str(e)}"
        )