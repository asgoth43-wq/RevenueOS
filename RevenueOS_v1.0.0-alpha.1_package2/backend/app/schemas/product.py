from decimal import Decimal
from pydantic import BaseModel, ConfigDict

class ProductCreate(BaseModel):
    project_id: int
    title: str
    category: str
    description: str | None = None
    price: Decimal = Decimal("0.00")

class ProductRead(ProductCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    status: str
