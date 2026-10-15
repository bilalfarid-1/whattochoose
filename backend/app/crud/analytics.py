from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.application import JobApplication
from app.models.interview import InterviewStage
from app.schemas.analytics import ApplicationMetricsRead

ALL_STATUSES = [
    "applied",
    "screening",
    "technical_interview",
    "behavioral_interview",
    "offer_received",
    "rejected",
    "withdrawn"
]

def get_user_metrics(db: Session, user_id: int) -> ApplicationMetricsRead:
    # Status counts
    counts_query = (
        db.query(JobApplication.status, func.count(JobApplication.id))
        .filter(JobApplication.user_id == user_id)
        .group_by(JobApplication.status)
        .all()
    )
    status_map = {status: 0 for status in ALL_STATUSES}
    total = 0
    for status, count in counts_query:
        status_map[status] = count
        total += count

    active = sum(status_map[s] for s in ALL_STATUSES if s not in ["rejected", "withdrawn"])
    offers = status_map.get("offer_received", 0)
    rejections = status_map.get("rejected", 0)

    # Distinct applications with interview stages or interview statuses
    interview_apps_count = (
        db.query(func.count(func.distinct(JobApplication.id)))
        .outerjoin(InterviewStage, InterviewStage.application_id == JobApplication.id)
        .filter(
            JobApplication.user_id == user_id,
            (JobApplication.status.in_(["technical_interview", "behavioral_interview", "offer_received"]))
            | (InterviewStage.id.isnot(None))
        )
        .scalar() or 0
    )

    responded_apps = total - status_map.get("applied", 0)
    response_rate = round((responded_apps / total * 100.0), 1) if total > 0 else 0.0
    interview_conversion = round((interview_apps_count / total * 100.0), 1) if total > 0 else 0.0

    return ApplicationMetricsRead(
        total_applications=total,
        active_applications=active,
        interviews_scheduled=interview_apps_count,
        offers_received=offers,
        rejections=rejections,
        response_rate_pct=response_rate,
        interview_conversion_pct=interview_conversion,
        by_status=status_map
    )
