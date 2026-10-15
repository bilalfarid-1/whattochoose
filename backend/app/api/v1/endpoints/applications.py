from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.application import (
    JobApplicationCreate,
    JobApplicationRead,
    JobApplicationUpdate,
    JobApplicationDetail
)
from app.crud.application import get_by_id, get_multi, create, update, delete
from app.crud.company import get_by_id as get_company_by_id

router = APIRouter()

@router.get("/", response_model=List[JobApplicationRead])
def list_applications(
    status: Optional[str] = Query(None, description="Filter by application status"),
    company_id: Optional[int] = Query(None, description="Filter by company ID"),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Retrieve all job applications for the authenticated user with optional filtering."""
    return get_multi(
        db=db,
        user_id=current_user.id,
        status=status,
        company_id=company_id,
        skip=skip,
        limit=limit
    )

@router.post("/", response_model=JobApplicationRead, status_code=status.HTTP_201_CREATED)
def create_application(
    app_in: JobApplicationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new job application tracked under the current user."""
    company = get_company_by_id(db, company_id=app_in.company_id)
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Company with ID {app_in.company_id} does not exist."
        )
    return create(db=db, obj_in=app_in, user_id=current_user.id)

@router.get("/{application_id}", response_model=JobApplicationDetail)
def get_application_detail(
    application_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Retrieve comprehensive details of a specific application including company info, interviews, and notes."""
    app_obj = get_by_id(db=db, application_id=application_id, user_id=current_user.id)
    if not app_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found."
        )
    return app_obj

@router.patch("/{application_id}", response_model=JobApplicationRead)
def update_application(
    application_id: int,
    app_update: JobApplicationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update application attributes such as status, job title, salary range, or deadline."""
    app_obj = get_by_id(db=db, application_id=application_id, user_id=current_user.id)
    if not app_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found."
        )
    return update(db=db, db_obj=app_obj, obj_in=app_update)

@router.delete("/{application_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_application(
    application_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete an application and its associated interviews and notes."""
    app_obj = get_by_id(db=db, application_id=application_id, user_id=current_user.id)
    if not app_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found."
        )
    delete(db=db, db_obj=app_obj)
    return None
