from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class InterviewStageBase(BaseModel):
    stage_name: str = Field(..., min_length=1, max_length=100)
    scheduled_at: Optional[datetime] = None
    interviewer_notes: Optional[str] = None
    outcome: str = Field(default="pending", pattern="^(pending|passed|failed)$")

class InterviewStageCreate(InterviewStageBase):
    pass

class InterviewStageUpdate(BaseModel):
    stage_name: Optional[str] = Field(None, min_length=1, max_length=100)
    scheduled_at: Optional[datetime] = None
    interviewer_notes: Optional[str] = None
    outcome: Optional[str] = Field(None, pattern="^(pending|passed|failed)$")

class InterviewStageRead(InterviewStageBase):
    id: int
    application_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
