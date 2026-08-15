from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.api.auth import get_current_user
from backend.app.db.session import get_db
from backend.app.models.affiliate import AffiliateLink, AffiliateProgram
from backend.app.models.product import Product
from backend.app.models.project import Project
from backend.app.models.user import User
from backend.app.schemas.affiliate import AffiliateClickResponse, AffiliateLinkCreate, AffiliateLinkRead, AffiliateProgramCreate, AffiliateProgramRead

router = APIRouter(prefix="/affiliates")

@router.post("/programs", response_model=AffiliateProgramRead, status_code=201)
def create_program(payload: AffiliateProgramCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if db.query(AffiliateProgram).filter(AffiliateProgram.name == payload.name).first():
        raise HTTPException(status_code=409, detail="Affiliate program already exists")
    program = AffiliateProgram(**payload.model_dump())
    db.add(program); db.commit(); db.refresh(program)
    return program

@router.get("/programs", response_model=list[AffiliateProgramRead])
def list_programs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(AffiliateProgram).order_by(AffiliateProgram.name.asc()).all()

@router.post("/links", response_model=AffiliateLinkRead, status_code=201)
def create_link(payload: AffiliateLinkCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not db.get(AffiliateProgram, payload.program_id):
        raise HTTPException(status_code=404, detail="Affiliate program not found")
    if payload.product_id is not None:
        product = db.query(Product).join(Project).filter(Product.id == payload.product_id, Project.owner_id == current_user.id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
    link = AffiliateLink(**payload.model_dump())
    db.add(link); db.commit(); db.refresh(link)
    return link

@router.get("/links", response_model=list[AffiliateLinkRead])
def list_links(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(AffiliateLink).outerjoin(Product).outerjoin(Project).filter(
        (Project.owner_id == current_user.id) | (AffiliateLink.product_id.is_(None))
    ).order_by(AffiliateLink.id.desc()).all()

@router.post("/links/{link_id}/click", response_model=AffiliateClickResponse)
def register_click(link_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    link = db.get(AffiliateLink, link_id)
    if not link:
        raise HTTPException(status_code=404, detail="Affiliate link not found")
    if link.product_id is not None:
        owned = db.query(Product).join(Project).filter(Product.id == link.product_id, Project.owner_id == current_user.id).first()
        if not owned:
            raise HTTPException(status_code=404, detail="Affiliate link not found")
    link.clicks += 1
    db.commit(); db.refresh(link)
    return AffiliateClickResponse(id=link.id, clicks=link.clicks)
