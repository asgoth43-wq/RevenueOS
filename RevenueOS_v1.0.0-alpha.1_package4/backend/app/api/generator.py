from fastapi import APIRouter, Depends, HTTPException
from backend.app.api.auth import get_current_user
from backend.app.models.user import User
from backend.app.schemas.generator import ProductGenerateRequest, ProductGenerateResponse
from backend.app.services.product_engine import build_product

router = APIRouter(prefix="/generator")

@router.post("/product", response_model=ProductGenerateResponse)
def generate_product(payload: ProductGenerateRequest, current_user: User = Depends(get_current_user)):
    try:
        draft = build_product(payload.topic, payload.category)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    return ProductGenerateResponse(
        title=draft.title,
        category=draft.category,
        description=draft.description,
        sections=draft.sections,
        tags=draft.tags,
        suggested_price=draft.suggested_price,
    )
