from datetime import datetime, timezone, date
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    job_title = Column(String(150), nullable=False, index=True)
    job_url = Column(String(500), nullable=True)
    salary_range = Column(String(100), nullable=True)
    work_location = Column(String(50), default="remote", nullable=False) # remote, hybrid, on-site
    status = Column(String(50), default="applied", nullable=False, index=True) # applied, screening, technical, interview, offer, rejected, withdrawn
    applied_date = Column(Date, default=date.today, nullable=False)
    deadline = Column(Date, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    user = relationship("User", back_populates="applications")
    company = relationship("Company", back_populates="applications")
    interviews = relationship("InterviewStage", back_populates="application", cascade="all, delete-orphan", order_by="InterviewStage.scheduled_at")
    notes = relationship("ApplicationNote", back_populates="application", cascade="all, delete-orphan", order_by="desc(ApplicationNote.created_at)")
