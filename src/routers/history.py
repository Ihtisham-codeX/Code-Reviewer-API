from fastapi import APIRouter, Depends
from src.services import history_service
from src.security.dependencies import get_current_user

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


# Get my review history
@router.get("/")
def get_history(current_user = Depends(get_current_user)):
    return history_service.get_my_history(current_user["user_id"])
