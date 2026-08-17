from fastapi import APIRouter
from backend.app.api.health import router as health_router
from backend.app.api.auth import router as auth_router
from backend.app.api.projects import router as projects_router
from backend.app.api.products import router as products_router
from backend.app.api.revenues import router as revenues_router
from backend.app.api.generator import router as generator_router
from backend.app.api.export import router as export_router
from backend.app.api.seo import router as seo_router
from backend.app.api.affiliates import router as affiliates_router
from backend.app.api.marketplace import router as marketplace_router
from backend.app.api.analytics import router as analytics_router
from backend.app.api.dashboard import router as dashboard_router

api_router = APIRouter()
for r in [health_router, auth_router, projects_router, products_router, revenues_router,
          generator_router, export_router, seo_router, affiliates_router,
          marketplace_router, analytics_router, dashboard_router]:
    api_router.include_router(r)
