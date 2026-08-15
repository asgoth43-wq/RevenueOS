from fastapi import APIRouter, Depends, HTTPException
from backend.app.api.auth import get_current_user
from backend.app.models.user import User
from backend.app.schemas.marketplace import ListingRequest, ListingResponse, TrackingRequest, TrackingResponse
from backend.app.services.marketplace_service import add_tracking, build_listing
from backend.app.services.product_engine import build_product

router = APIRouter(prefix="/marketplace")

@router.post("/listing", response_model=ListingResponse)
def generate_listing(payload: ListingRequest, current_user: User = Depends(get_current_user)):
    try:
        draft = build_product(payload.topic, payload.category)
        listing = build_listing(draft, payload.marketplace, str(payload.destination_url))
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    return ListingResponse(**listing.__dict__)

@router.post("/tracking", response_model=TrackingResponse)
def generate_tracking_url(payload: TrackingRequest, current_user: User = Depends(get_current_user)):
    return TrackingResponse(
        tracked_url=add_tracking(str(payload.url), payload.source, payload.campaign)
    )
