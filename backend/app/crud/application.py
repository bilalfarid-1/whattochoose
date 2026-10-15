from typing import Optional, List
from sqlalchemy.orm import Session, joinedload
from app.models.application import JobApplication
from app.schemas.application import JobApplicationCreate, JobApplicationUpdate

def get_by_id(db: Session, application_id: int, user_id: int) -> Optional[JobApplication]:
    return (
        db.query(JobApplication)
        .options(
            joinedload(JobApplication.company),
            joinedload(JobApplication.interviews),
            joinedload(JobApplication.notes)
        )
        .filter(JobApplication.id == application_id, JobApplication.user_id == user_id)
        .first()
    )

def get_multi(
    db: Session,
    user_id: int,
    status: Optional[str] = None,
    company_id: Optional[int] = None,
    skip: int = 0,
    limit: int = 50
) -> List[JobApplication]:
    query = (
        db.query(JobApplication)
        .options(joinedload(JobApplication.company))
        .filter(JobApplication.user_id == user_id)
    )
    if status:
        query = query.filter(JobApplication.status == status)
    if company_id:
        query = query.filter(JobApplication.company_id == company_id)
    
    return query.order_by(JobApplication.applied_date.desc()).offset(skip).limit(limit).all()

def create(db: Session, obj_in: JobApplicationCreate, user_id: int) -> JobApplication:
    db_obj = JobApplication(
        user_id=user_id,
        company_id=obj_in.company_id,
        job_title=obj_in.job_title.strip(),
        job_url=obj_in.job_url,
        salary_range=obj_in.salary_range,
        work_location=obj_in.work_location,
        status=obj_in.status,
        applied_date=obj_in.applied_date,
        deadline=obj_in.deadline
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update(db: Session, db_obj: JobApplication, obj_in: JobApplicationUpdate) -> JobApplication:
    update_data = obj_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete(db: Session, db_obj: JobApplication) -> None:
    db.delete(db_obj)
    db.commit()
