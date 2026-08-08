from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.db.session import get_db
from backend.app.models.project import Project
from backend.app.schemas.project import ProjectCreate, ProjectRead

router = APIRouter(prefix="/projects")

@router.post("", response_model=ProjectRead)
def create_project(payload: ProjectCreate, db: Session = Depends(get_db)):
    project = Project(owner_id=1, name=payload.name, description=payload.description)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

@router.get("", response_model=list[ProjectRead])
def list_projects(db: Session = Depends(get_db)):
    return db.query(Project).order_by(Project.id.desc()).all()
