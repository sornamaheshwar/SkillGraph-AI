from fastapi import APIRouter

from backend.app.schemas.role import JobRole
from backend.app.services.roles import get_all_roles


router = APIRouter(
    prefix="/api/roles",
    tags=["Job Roles"]
)


@router.get(
    "/",
    response_model=list[JobRole]
)
def get_roles():
    return get_all_roles()