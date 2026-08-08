import os

APP_NAME = os.getenv("APP_NAME", "RevenueOS")
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://revenueos:revenueos@db:5432/revenueos",
)
SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
