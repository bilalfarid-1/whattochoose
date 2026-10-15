from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class InterviewStage(Base):
    __tablename__ = "interview_stages"

    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("job_applications.id", ondelete="CASCADE"), nullable=False, index=True)
    stage_name = Column(String(100), nullable=False) # e.g. HR Screening, Technical Round, System Design, Final Culture
    scheduled_at = Column(DateTime, nullable=True)
    interviewer_notes = Column(Text, nullable=True)
    outcome = Column(String(50), default="pending", nullable=False) # pending, passed, failed
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    application = relationship("JobApplication", back_populates="interviews")
