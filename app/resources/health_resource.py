from fastapi import APIRouter

router = APIRouter()

router.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Cheap health check"""
    return {"status": "ok"}




