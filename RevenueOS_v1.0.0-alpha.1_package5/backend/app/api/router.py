from fastapi import APIRouter
from backend.app.api.health import router as health_router
from backend.app.api.auth import router as auth_router
from backend.app.api.projects import router as projects_router
from backend.app.api.products import router as products_router
from backend.app.api.revenues import router as revenues_router
from backend.app.api.generator import router as generator_router
from backend.app.api.export import router as export_router
from backend.app.api.seo import router as seo_router

api_router = APIRouter()
api_router.include_router(health_router, tags=["health"])
api_router.include_router(auth_router, tags=["auth"])
api_router.include_router(projects_router, tags=["projects"])
api_router.include_router(products_router, tags=["products"])
api_router.include_router(revenues_router, tags=["revenues"])
api_router.include_router(generator_router, tags=["generator"])
api_router.include_router(export_router, tags=["export"])
api_router.include_router(seo_router, tags=["seo"])
