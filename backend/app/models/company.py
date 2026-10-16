from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base

class Company(Base):
    """
    Globally shared directory of public company metadata (name, website, industry, location).
    Shared across all authenticated users. Personal candidate notes, recruiter contacts,
    and interview debriefs MUST NOT be stored here; they belong exclusively in user-scoped
    ApplicationNote and JobApplication records.
    """
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True, index=True, nullable=False)
    website = Column(String(255), nullable=True)
    industry = Column(String(100), nullable=True)
    location = Column(String(150), nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    applications = relationship("JobApplication", back_populates="company", cascade="all, delete-orphan")
