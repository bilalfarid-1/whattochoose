from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.interview import InterviewStageCreate, InterviewStageRead, InterviewStageUpdate
from app.crud.interview import create, get_by_application, get_by_id, update
from app.crud.application import get_by_id as get_application_by_id

router = APIRouter()

@router.get("/applications/{application_id}/interviews", response_model=List[InterviewStageRead])
def list_application_interviews(
    application_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List all interview rounds for an application."""
    app_obj = get_application_by_id(db=db, application_id=application_id, user_id=current_user.id)
    if not app_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found."
        )
    return get_by_application(db=db, application_id=application_id)

@router.post("/applications/{application_id}/interviews", response_model=InterviewStageRead, status_code=status.HTTP_201_CREATED)
def create_interview_stage(
    application_id: int,
    stage_in: InterviewStageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Schedule or record a new interview round."""
    app_obj = get_application_by_id(db=db, application_id=application_id, user_id=current_user.id)
    if not app_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found."
        )
    return create(db=db, application_id=application_id, obj_in=stage_in)

@router.patch("/interviews/{interview_id}", response_model=InterviewStageRead)
def update_interview_stage(
    interview_id: int,
    stage_update: InterviewStageUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update interview stage notes, scheduled time, or outcome."""
    stage = get_by_id(db=db, interview_id=interview_id)
    if not stage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview stage not found."
        )
    # Verify ownership
    app_obj = get_application_by_id(db=db, application_id=stage.application_id, user_id=current_user.id)
    if not app_obj:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to edit this interview stage."
        )
    return update(db=db, db_obj=stage, obj_in=stage_update)
