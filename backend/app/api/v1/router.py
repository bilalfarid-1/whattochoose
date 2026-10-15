from fastapi import APIRouter
from app.api.v1.endpoints import auth, companies, applications, interviews, notes, analytics

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(companies.router, prefix="/companies", tags=["Companies"])
api_router.include_router(applications.router, prefix="/applications", tags=["Job Applications"])
api_router.include_router(interviews.router, tags=["Interviews"])
api_router.include_router(notes.router, tags=["Notes & Debriefs"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Funnel Analytics"])
