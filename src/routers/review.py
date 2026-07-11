from fastapi import APIRouter, Depends
from src.models.review import ReviewRequest
from src.services import review_service
from src.security.dependencies import get_current_user

router = APIRouter(
    prefix="/review",
    tags=["Review"]
)


# Review code
@router.post("/")
def review_code(request: ReviewRequest, current_user = Depends(get_current_user)):
    return review_service.review_code(
        request.project_id,
        request.filename,
        request.code,
        current_user["user_id"]
    )
