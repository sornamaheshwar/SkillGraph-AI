from pydantic import BaseModel


class ProjectRecommendation(BaseModel):
    id: str
    name: str
    description: str
    difficulty: str
    missing_skills_covered: list[str]
    relevance_score: int


class ImplementationStep(BaseModel):
    step: int
    title: str
    description: str


class ProjectDetails(BaseModel):
    id: str
    name: str
    description: str
    difficulty: str

    skills: list[str]

    tech_stack: list[str]

    key_features: list[str]

    architecture: list[str]

    implementation_steps: list[ImplementationStep]