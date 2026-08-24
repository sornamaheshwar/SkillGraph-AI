from fastapi import APIRouter

from backend.app.schemas.profile import Profile
from backend.app.services.profile import get_user_profile


router = APIRouter(
    prefix="/api/profile",
    tags=["Profile"]
)


# ============================================================
# GET USER PROFILE
# ============================================================

@router.get(
    "/",
    response_model=Profile
)
def get_profile():
    return get_user_profile()