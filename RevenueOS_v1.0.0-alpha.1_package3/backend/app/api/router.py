from fastapi import APIRouter
from backend.app.api.health import router as health_router
from backend.app.api.auth import router as auth_router
from backend.app.api.projects import router as projects_router
from backend.app.api.products import router as products_router
from backend.app.api.revenues import router as revenues_router

api_router = APIRouter()
api_router.include_router(health_router, tags=["health"])
api_router.include_router(auth_router, tags=["auth"])
api_router.include_router(projects_router, tags=["projects"])
api_router.include_router(products_router, tags=["products"])
api_router.include_router(revenues_router, tags=["revenues"])
