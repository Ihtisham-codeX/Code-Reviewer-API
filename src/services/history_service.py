from src.respositories import review_repo
from src.utils.helpers import format_review_row


########################### GET MY REVIEW HISTORY ###########################
def get_my_history(user_id: int):
    rows = review_repo.get_reviews_by_user(user_id)

    history = []
    for row in rows:
        history.append(format_review_row(row))

    return history
