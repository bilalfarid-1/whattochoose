from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class ApplicationNoteBase(BaseModel):
    content: str = Field(..., min_length=1, description="Note content or debrief details")

class ApplicationNoteCreate(ApplicationNoteBase):
    pass

class ApplicationNoteRead(ApplicationNoteBase):
    id: int
    application_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
