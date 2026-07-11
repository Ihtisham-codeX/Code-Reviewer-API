from src.connection.database import conn
import json


########################### SAVE REVIEW ###########################
def save_review(project_id: int, user_id: int, filename: str, ai_result: dict):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Reviews(project_id, user_id, filename, score, readability, accuracy, best_practices, bugs, security, suggestions, optimized_code)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING review_id
    """, (
        project_id,
        user_id,
        filename,
        ai_result["score"],
        ai_result["readability"],
        ai_result["accuracy"],
        ai_result["best_practices"],
        json.dumps(ai_result["bugs"]),
        ai_result["security"],
        json.dumps(ai_result["suggestions"]),
        ai_result["optimized_code"]
    ))

    row = cursor.fetchone()
    conn.commit()
    cursor.close()
    return row[0]


########################### GET REVIEW BY ID ###########################
def get_review_by_id(review_id: int):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM Reviews
        WHERE review_id = %s
    """, (review_id,))

    row = cursor.fetchone()
    cursor.close()
    return row


########################### GET REVIEWS BY USER ###########################
def get_reviews_by_user(user_id: int):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM Reviews
        WHERE user_id = %s
        ORDER BY created_at DESC
    """, (user_id,))

    rows = cursor.fetchall()
    cursor.close()
    return rows


########################### COUNT REVIEWS IN LAST HOUR ###########################
def count_recent_reviews(user_id: int):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(*)
        FROM Reviews
        WHERE user_id = %s
        AND created_at >= NOW() - INTERVAL '1 hour'
    """, (user_id,))

    count = cursor.fetchone()[0]
    cursor.close()
    return count
