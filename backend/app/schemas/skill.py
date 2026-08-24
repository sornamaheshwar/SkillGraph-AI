from pydantic import BaseModel


# ============================================================
# SKILL
# ============================================================

class Skill(BaseModel):
    id: str
    name: str
    category: str


# ============================================================
# USER SKILL REQUEST
# ============================================================

class UserSkillRequest(BaseModel):
    skill_id: str


# ============================================================
# SKILL GAP
# ============================================================

class SkillGap(BaseModel):
    id: str
    name: str
    importance: str
    weight: int


# ============================================================
# LEARNING PATH
# ============================================================

class LearningPath(BaseModel):
    path: list[str]
    hops: int