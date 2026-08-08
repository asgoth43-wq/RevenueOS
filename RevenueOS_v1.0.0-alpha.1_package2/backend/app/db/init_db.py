from backend.app.db.base import Base
from backend.app.db.session import engine
from backend.app.models import User, Project, Product, Revenue

def init_db() -> None:
    Base.metadata.create_all(bind=engine)
