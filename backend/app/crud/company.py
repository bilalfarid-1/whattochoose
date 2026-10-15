from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate

def get_by_id(db: Session, company_id: int) -> Optional[Company]:
    return db.query(Company).filter(Company.id == company_id).first()

def get_by_name(db: Session, name: str) -> Optional[Company]:
    return db.query(Company).filter(Company.name.ilike(name.strip())).first()

def get_multi(db: Session, skip: int = 0, limit: int = 50) -> List[Company]:
    return db.query(Company).order_by(Company.name.asc()).offset(skip).limit(limit).all()

def create(db: Session, obj_in: CompanyCreate) -> Company:
    db_obj = Company(
        name=obj_in.name.strip(),
        website=obj_in.website.strip() if obj_in.website else None,
        location=obj_in.location.strip() if obj_in.location else None,
        notes=obj_in.notes
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_or_create(db: Session, obj_in: CompanyCreate) -> Company:
    existing = get_by_name(db, obj_in.name)
    if existing:
        return existing
    return create(db, obj_in)
