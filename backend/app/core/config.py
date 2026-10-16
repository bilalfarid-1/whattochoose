from typing import List
from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "JobPulse API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    AUTO_CREATE_TABLES: bool = False
    
    SECRET_KEY: str = "super-secret-development-key-change-in-production-min-32-chars"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    DATABASE_URL: str = "sqlite:///./jobpulse.db"
    
    # CORS Origins
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    @model_validator(mode="after")
    def validate_production_security(self):
        if self.ENVIRONMENT.lower() == "production":
            insecure_placeholders = [
                "super-secret-development-key-change-in-production-min-32-chars",
                "production-secure-random-token-key-replace-in-env",
                "CHANGE_THIS",
                "secret",
            ]
            if any(p in self.SECRET_KEY for p in insecure_placeholders) or len(self.SECRET_KEY) < 32:
                raise ValueError(
                    "Production security violation: In production environment, SECRET_KEY must be "
                    "explicitly set via environment variable with a secure random token of at least 32 characters."
                )
        return self

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="allow"
    )

settings = Settings()
