from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.note import ApplicationNoteCreate, ApplicationNoteRead
from app.crud.note import create, get_by_application
from app.crud.application import get_by_id as get_application_by_id

router = APIRouter()

@router.get("/applications/{application_id}/notes", response_model=List[ApplicationNoteRead])
def list_application_notes(
    application_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List all notes and debrief entries for a specific application."""
    app_obj = get_application_by_id(db=db, application_id=application_id, user_id=current_user.id)
    if not app_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found."
        )
    return get_by_application(db=db, application_id=application_id)

@router.post("/applications/{application_id}/notes", response_model=ApplicationNoteRead, status_code=status.HTTP_201_CREATED)
def create_application_note(
    application_id: int,
    note_in: ApplicationNoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Add a new journal note, referral contact, or debrief insight to an application."""
    app_obj = get_application_by_id(db=db, application_id=application_id, user_id=current_user.id)
    if not app_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found."
        )
    return create(db=db, application_id=application_id, obj_in=note_in)
