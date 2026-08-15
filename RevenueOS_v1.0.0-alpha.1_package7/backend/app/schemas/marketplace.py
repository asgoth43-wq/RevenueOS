from pydantic import BaseModel, Field, HttpUrl

class ListingRequest(BaseModel):
    topic: str = Field(min_length=3, max_length=300)
    category: str = Field(default="digital-product", max_length=100)
    marketplace: str = Field(min_length=2, max_length=50)
    destination_url: HttpUrl

class ListingResponse(BaseModel):
    marketplace: str
    title: str
    description: str
    price: str
    tags: list[str]
    destination_url: str

class TrackingRequest(BaseModel):
    url: HttpUrl
    source: str = Field(min_length=1, max_length=50)
    campaign: str = Field(min_length=1, max_length=100)

class TrackingResponse(BaseModel):
    tracked_url: str
