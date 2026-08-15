from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field, HttpUrl

class AffiliateProgramCreate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    network: str = Field(min_length=2, max_length=100)
    signup_url: HttpUrl | None = None
    commission_rate: Decimal = Field(default=Decimal("0"), ge=0, le=100)

class AffiliateProgramRead(AffiliateProgramCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    status: str

class AffiliateLinkCreate(BaseModel):
    program_id: int
    product_id: int | None = None
    url: HttpUrl
    label: str | None = Field(default=None, max_length=200)

class AffiliateLinkRead(AffiliateLinkCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    clicks: int
    conversions: int

class AffiliateClickResponse(BaseModel):
    id: int
    clicks: int
