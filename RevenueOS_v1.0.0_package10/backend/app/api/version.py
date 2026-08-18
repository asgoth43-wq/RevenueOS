from fastapi import APIRouter

router = APIRouter()

@router.get("/version")
def version():
    return {
        "name": "RevenueOS",
        "version": "1.0.0",
        "status": "release-candidate"
    }
