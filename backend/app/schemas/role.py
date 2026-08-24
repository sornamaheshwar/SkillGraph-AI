from pydantic import BaseModel


class JobRole(BaseModel):
    id: str
    name: str
    description: str