from pydantic import BaseModel, Field

class ExportRequest(BaseModel):
    topic: str = Field(min_length=3, max_length=300)
    category: str = Field(default="digital-product", max_length=100)

class ExportResponse(BaseModel):
    filename: str
    manifest: dict
