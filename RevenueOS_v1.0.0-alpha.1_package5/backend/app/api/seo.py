from fastapi import APIRouter, Depends
from backend.app.api.auth import get_current_user
from backend.app.models.user import User
from backend.app.schemas.seo import SEORequest, SEOResponse
from backend.app.services.product_engine import build_product
from backend.app.services.seo_service import build_seo

router = APIRouter(prefix="/seo")

@router.post("/generate", response_model=SEOResponse)
def generate_seo(payload: SEORequest, current_user: User = Depends(get_current_user)):
    draft = build_product(payload.topic, payload.category)
    return SEOResponse(**build_seo(draft))
