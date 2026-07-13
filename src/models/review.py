from pydantic import BaseModel
from src.utils.enums import AIProvider


class ReviewRequest(BaseModel):
    project_id: int
    filename: str
    code: str
    provider: AIProvider = AIProvider.GEMINI

class ReviewResponse(BaseModel):
    review_id: int
    filename: str
    score: int
    readability: int
    accuracy: int
    best_practices: int
    bugs: list
    security: str
    suggestions: list
    optimized_code: str
