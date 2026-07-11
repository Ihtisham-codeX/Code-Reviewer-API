from fastapi import APIRouter, Depends
from src.security.dependencies import get_current_user

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


# Get my profile
@router.get("/profile")
def get_profile(current_user = Depends(get_current_user)):
    return {
        "user_id": current_user["user_id"],
        "email": current_user["email"]
    }
