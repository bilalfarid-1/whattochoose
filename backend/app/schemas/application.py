from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel, ConfigDict, Field
from app.schemas.company import CompanyRead
from app.schemas.interview import InterviewStageRead
from app.schemas.note import ApplicationNoteRead

STATUS_PATTERN = "^(applied|screening|technical_interview|behavioral_interview|offer_received|rejected|withdrawn)$"
LOCATION_PATTERN = "^(remote|hybrid|on-site)$"

class JobApplicationBase(BaseModel):
    company_id: int
    job_title: str = Field(..., min_length=2, max_length=150)
    job_url: Optional[str] = None
    salary_range: Optional[str] = None
    work_location: str = Field(default="remote", pattern=LOCATION_PATTERN)
    status: str = Field(default="applied", pattern=STATUS_PATTERN)
    applied_date: date = Field(default_factory=date.today)
    deadline: Optional[date] = None

class JobApplicationCreate(JobApplicationBase):
    pass

class JobApplicationUpdate(BaseModel):
    job_title: Optional[str] = Field(None, min_length=2, max_length=150)
    job_url: Optional[str] = None
    salary_range: Optional[str] = None
    work_location: Optional[str] = Field(None, pattern=LOCATION_PATTERN)
    status: Optional[str] = Field(None, pattern=STATUS_PATTERN)
    applied_date: Optional[date] = None
    deadline: Optional[date] = None

class JobApplicationRead(JobApplicationBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class JobApplicationDetail(JobApplicationRead):
    company: CompanyRead
    interviews: List[InterviewStageRead] = []
    notes: List[ApplicationNoteRead] = []

    model_config = ConfigDict(from_attributes=True)
