from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.interview import InterviewStage
from app.schemas.interview import InterviewStageCreate, InterviewStageUpdate

def get_by_id(db: Session, interview_id: int) -> Optional[InterviewStage]:
    return db.query(InterviewStage).filter(InterviewStage.id == interview_id).first()

def get_by_application(db: Session, application_id: int) -> List[InterviewStage]:
    return (
        db.query(InterviewStage)
        .filter(InterviewStage.application_id == application_id)
        .order_by(InterviewStage.scheduled_at.asc())
        .all()
    )

def create(db: Session, application_id: int, obj_in: InterviewStageCreate) -> InterviewStage:
    db_obj = InterviewStage(
        application_id=application_id,
        stage_name=obj_in.stage_name.strip(),
        scheduled_at=obj_in.scheduled_at,
        interviewer_notes=obj_in.interviewer_notes,
        outcome=obj_in.outcome
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update(db: Session, db_obj: InterviewStage, obj_in: InterviewStageUpdate) -> InterviewStage:
    update_data = obj_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
