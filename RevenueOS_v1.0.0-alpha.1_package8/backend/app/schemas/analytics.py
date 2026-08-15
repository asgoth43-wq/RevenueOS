from pydantic import BaseModel

class RevenueItem(BaseModel):
    source: str
    amount: float

class AnalyticsRequest(BaseModel):
    items: list[RevenueItem]

class AnalyticsResponse(BaseModel):
    total_revenue: float
    sources: dict[str, float]

class ConversionResponse(BaseModel):
    clicks: int
    conversions: int
    rate: float
