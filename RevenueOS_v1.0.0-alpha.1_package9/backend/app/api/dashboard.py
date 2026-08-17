from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.api.auth import get_current_user
from backend.app.db.session import get_db
from backend.app.models.user import User
from backend.app.models.revenue import Revenue
from backend.app.models.affiliate import AffiliateLink
from backend.app.services.dashboard_service import build_summary
from backend.app.schemas.dashboard import DashboardSummary

router = APIRouter(prefix="/dashboard")

@router.get("/summary", response_model=DashboardSummary)
def summary(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    revenues = db.query(Revenue).all()
    links = db.query(AffiliateLink).all()
    rows = [{"revenue": getattr(r, "amount", 0), "clicks": 0, "conversions": 0}
            for r in revenues]
    rows += [{"revenue": 0, "clicks": l.clicks, "conversions": l.conversions}
             for l in links]
    return build_summary(rows)
