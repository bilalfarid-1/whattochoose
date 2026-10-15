from typing import Dict
from pydantic import BaseModel

class ApplicationMetricsRead(BaseModel):
    total_applications: int
    active_applications: int
    interviews_scheduled: int
    offers_received: int
    rejections: int
    response_rate_pct: float
    interview_conversion_pct: float
    by_status: Dict[str, int]
