from fastapi import APIRouter, Depends
from backend.app.api.auth import get_current_user
from backend.app.models.user import User
from backend.app.schemas.analytics import AnalyticsRequest, AnalyticsResponse, ConversionResponse
from backend.app.services.analytics_service import revenue_summary, conversion_rate

router = APIRouter(prefix="/analytics")

@router.post("/revenue", response_model=AnalyticsResponse)
def revenue(payload: AnalyticsRequest, current_user: User = Depends(get_current_user)):
    data = [i.model_dump() for i in payload.items]
    return AnalyticsResponse(**revenue_summary(data))

@router.get("/conversion", response_model=ConversionResponse)
def conversion(clicks: int, conversions: int, current_user: User = Depends(get_current_user)):
    return ConversionResponse(
        clicks=clicks,
        conversions=conversions,
        rate=conversion_rate(clicks, conversions)
    )
