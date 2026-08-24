from pydantic import BaseModel


class Profile(BaseModel):
    user_id: str
    user_name: str
    target_role: str
    skills: list[str]