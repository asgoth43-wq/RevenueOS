from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.db.session import get_db
from backend.app.models.revenue import Revenue
from backend.app.schemas.revenue import RevenueCreate, RevenueRead

router = APIRouter(prefix="/revenues")

@router.post("", response_model=RevenueRead)
def create_revenue(payload: RevenueCreate, db: Session = Depends(get_db)):
    revenue = Revenue(**payload.model_dump())
    db.add(revenue)
    db.commit()
    db.refresh(revenue)
    return revenue

@router.get("", response_model=list[RevenueRead])
def list_revenues(db: Session = Depends(get_db)):
    return db.query(Revenue).order_by(Revenue.occurred_at.desc()).all()
