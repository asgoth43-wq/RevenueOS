import os

class Settings:
    app_env = os.getenv("APP_ENV", "development")
    secret_key = os.getenv("SECRET_KEY", "change-me")
    database_url = os.getenv("DATABASE_URL", "sqlite:///./revenueos.db")
    cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000")

settings = Settings()
