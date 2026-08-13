from fastapi import APIRouter, Depends, HTTPException
from backend.app.api.auth import get_current_user
from backend.app.models.user import User
from backend.app.schemas.export import ExportRequest, ExportResponse
from backend.app.services.export_service import build_manifest
from backend.app.services.product_engine import build_product

router = APIRouter(prefix="/export")

@router.post("/json", response_model=ExportResponse)
def export_product(payload: ExportRequest, current_user: User = Depends(get_current_user)):
    try:
        draft = build_product(payload.topic, payload.category)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    return ExportResponse(filename="product-manifest.json", manifest=build_manifest(draft))
