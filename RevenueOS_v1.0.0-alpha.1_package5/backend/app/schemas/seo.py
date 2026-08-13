from pydantic import BaseModel, Field

class SEORequest(BaseModel):
    topic: str = Field(min_length=3, max_length=300)
    category: str = Field(default="digital-product", max_length=100)

class SEOResponse(BaseModel):
    seo_title: str
    meta_description: str
    primary_keyword: str
    keywords: list[str]
