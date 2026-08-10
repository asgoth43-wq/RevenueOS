from decimal import Decimal
from pydantic import BaseModel, Field

class ProductGenerateRequest(BaseModel):
    topic: str = Field(min_length=3, max_length=300)
    category: str = Field(default="digital-product", max_length=100)

class ProductGenerateResponse(BaseModel):
    title: str
    category: str
    description: str
    sections: list[str]
    tags: list[str]
    suggested_price: Decimal
