from pydantic import BaseModel


class DashboardSummary(BaseModel):
    user_name: str
    target_role: str
    total_required_skills: int
    acquired_skills: int
    missing_skills: int
    readiness_score: float