from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.analytics import ApplicationMetricsRead
from app.crud.analytics import get_user_metrics

router = APIRouter()

@router.get("/", response_model=ApplicationMetricsRead)
def get_analytics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Calculate aggregated funnel metrics, conversion ratios, and status breakdown for the current user."""
    return get_user_metrics(db=db, user_id=current_user.id)
