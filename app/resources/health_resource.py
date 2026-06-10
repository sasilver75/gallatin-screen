from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health() -> dict[str, str]:
    """Cheap health check"""
    return {"status": "ok"}



