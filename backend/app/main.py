from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.core.config import settings
from backend.app.core.database import db

from backend.app.routers.roles import router as roles_router
from backend.app.routers.dashboard import router as dashboard_router
from backend.app.routers.skills import router as skills_router
from backend.app.routers.projects import router as projects_router
from backend.app.routers.learning_paths import (
    router as learning_paths_router,
)
from backend.app.routers.profile import router as profile_router


app = FastAPI(
    title="SkillGraph AI",
    description="Graph-powered skill intelligence and career planning platform.",
    version="1.0.0",
)


# ============================================================
# CORS
# ============================================================

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
     settings.frontend_url,
]

# Add deployed frontend URL if configured
if settings.frontend_url:
    origins.append(settings.frontend_url)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# STARTUP / SHUTDOWN
# ============================================================

@app.on_event("startup")
def startup_event():
    try:
        db.verify_connection()
        print("SkillGraph AI API connected to CognoDB.")
    except Exception as e:
        print(f"Database connection failed: {e}")


@app.on_event("shutdown")
def shutdown_event():
    db.close()
    print("CognoDB connection closed.")


# ============================================================
# ROUTERS
# ============================================================

app.include_router(roles_router)
app.include_router(dashboard_router)
app.include_router(skills_router)
app.include_router(projects_router)
app.include_router(learning_paths_router)
app.include_router(profile_router)


# ============================================================
# BASIC ENDPOINTS
# ============================================================

@app.get("/")
def root():
    return {
        "message": "Welcome to SkillGraph AI API"
    }


@app.get("/health")
def health():
    try:
        db.driver.verify_connectivity()

        return {
            "status": "healthy",
            "database": "connected",
        }

    except Exception:
        return {
            "status": "unhealthy",
            "database": "disconnected",
        }