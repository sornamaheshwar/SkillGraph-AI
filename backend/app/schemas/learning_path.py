from pydantic import BaseModel


class LearningPath(BaseModel):
    path: list[str]
    hops: int