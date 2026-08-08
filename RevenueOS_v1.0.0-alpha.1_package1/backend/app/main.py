from fastapi import FastAPI
from backend.app.api.router import api_router

app = FastAPI(title="RevenueOS", version="1.0.0-alpha.1")
app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
    return {"name": "RevenueOS", "version": "1.0.0-alpha.1", "status": "ok"}
