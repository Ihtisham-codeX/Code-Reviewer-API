from src.respositories import project_repo, review_repo
from src.services.ai import gemini_service
from src.utils.validators import validate_code_size, validate_language
from src.utils.helpers import format_review_row
from src.config.constants import MAX_REVIEWS_PER_HOUR
from src.exceptions.handlers import (
    ProjectNotFoundException,
    CodeTooLargeException,
    UnsupportedFileTypeException,
    RateLimitExceededException
)
from src.services.ai.ai_factory_pattern import AIFactory
from src.utils.enums import AIProvider


########################### REVIEW CODE ###########################
def review_code(project_id: int, filename: str, code: str, user_id: int , provider : AIProvider = AIProvider.GEMINI ):

    # Check if project exists
    project = project_repo.get_project_by_id(project_id)
    if project is None:
        raise ProjectNotFoundException()

    # Check code size
    if not validate_code_size(code):
        raise CodeTooLargeException()

    # Check if language is supported
    if not validate_language(filename):
        raise UnsupportedFileTypeException()

    # Enforce rate limit — max 5 reviews per hour
    recent_count = review_repo.count_recent_reviews(user_id)
    if recent_count >= MAX_REVIEWS_PER_HOUR:
        raise RateLimitExceededException()

    # Send code to ai factory that will select the provider based on request for review
    ai_service = AIFactory.get_ai(provider)

    ai_result = ai_service.review_code(code, filename)

    # Save review to database
    review_id = review_repo.save_review(project_id, user_id, filename, ai_result)

    # Return the full review result
    return {
        "review_id": review_id,
        "filename": filename,
        **ai_result
    }
