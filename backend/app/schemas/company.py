from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class CompanyBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=150)
    website: Optional[str] = None
    industry: Optional[str] = None
    location: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=150)
    website: Optional[str] = None
    industry: Optional[str] = None
    location: Optional[str] = None

class CompanyRead(CompanyBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
