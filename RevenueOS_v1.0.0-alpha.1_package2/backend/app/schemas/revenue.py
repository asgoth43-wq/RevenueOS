from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class RevenueCreate(BaseModel):
    product_id: int
    marketplace: str
    amount: Decimal
    currency: str = "EUR"

class RevenueRead(RevenueCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    occurred_at: datetime
