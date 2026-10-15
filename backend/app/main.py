from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import Base, engine
from app.api.v1.router import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ensure database schema tables exist on application startup
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=(
        "JobPulse API is a production-grade backend for engineering job search tracking. "
        "It provides structured application funnel analytics, company tracking, interview round management, "
        "and JWT-authenticated relational workflows designed to demonstrate enterprise Python engineering excellence."
    ),
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Configure CORS Middleware
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Include API Routers
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint to verify service availability and runtime status."""
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION
    }

import os
from fastapi.responses import HTMLResponse

FRONTEND_FILE_STATIC = os.path.abspath(os.path.join(os.path.dirname(__file__), "static", "index.html"))
FRONTEND_FILE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "frontend", "index.html"))

@app.get("/", response_class=HTMLResponse, tags=["Dashboard"])
@app.get("/dashboard", response_class=HTMLResponse, tags=["Dashboard"])
def get_dashboard():
    """Serve the interactive JobPulse frontend dashboard and research intelligence platform."""
    target_file = FRONTEND_FILE_STATIC if os.path.exists(FRONTEND_FILE_STATIC) else FRONTEND_FILE_ROOT
    if os.path.exists(target_file):
        with open(target_file, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<h1>JobPulse API</h1><p>Visit <a href='/docs'>/docs</a> for interactive OpenAPI documentation.</p>")

@app.get("/api", tags=["Root"])
def root_api():
    """API metadata and documentation entrypoint."""
    return {
        "message": f"Welcome to {settings.PROJECT_NAME}",
        "documentation": "/docs",
        "health": "/health",
        "api_v1": settings.API_V1_STR
    }
