from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.note import ApplicationNote
from app.schemas.note import ApplicationNoteCreate

def get_by_id(db: Session, note_id: int) -> Optional[ApplicationNote]:
    return db.query(ApplicationNote).filter(ApplicationNote.id == note_id).first()

def get_by_application(db: Session, application_id: int) -> List[ApplicationNote]:
    return (
        db.query(ApplicationNote)
        .filter(ApplicationNote.application_id == application_id)
        .order_by(ApplicationNote.created_at.desc())
        .all()
    )

def create(db: Session, application_id: int, obj_in: ApplicationNoteCreate) -> ApplicationNote:
    db_obj = ApplicationNote(
        application_id=application_id,
        content=obj_in.content.strip()
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete(db: Session, db_obj: ApplicationNote) -> None:
    db.delete(db_obj)
    db.commit()
