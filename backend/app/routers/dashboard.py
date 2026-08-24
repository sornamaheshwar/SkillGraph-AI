from fastapi import APIRouter

from backend.app.schemas.dashboard import DashboardSummary
from backend.app.services.dashboard import get_dashboard_summary


router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/",
    response_model=DashboardSummary
)
def get_dashboard():
    return get_dashboard_summary()