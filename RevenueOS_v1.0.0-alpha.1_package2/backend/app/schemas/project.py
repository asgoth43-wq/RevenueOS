from pydantic import BaseModel, ConfigDict

class ProjectCreate(BaseModel):
    name: str
    description: str | None = None

class ProjectRead(ProjectCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    owner_id: int
    status: str
