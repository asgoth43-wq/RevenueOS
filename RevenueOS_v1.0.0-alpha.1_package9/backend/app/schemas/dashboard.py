from decimal import Decimal
from pydantic import BaseModel

class DashboardSummary(BaseModel):
    items: int
    revenue: Decimal
    clicks: int
    conversions: int
    conversion_rate: float
