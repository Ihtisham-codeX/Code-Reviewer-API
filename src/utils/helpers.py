import json


def parse_ai_response(raw_text: str) -> dict:
    # AI sometimes wraps JSON in markdown code blocks, strip that
    cleaned = raw_text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("```")[1]
        if cleaned.startswith("json"):
            cleaned = cleaned[4:]

    return json.loads(cleaned.strip())


def format_review_row(row) -> dict:
    # Converts a database row into a clean review dictionary
    return {
        "review_id": row[0],
        "project_id": row[1],
        "user_id": row[2],
        "filename": row[3],
        "score": row[4],
        "readability": row[5],
        "accuracy": row[6],
        "best_practices": row[7],
        "bugs": json.loads(row[8]) if row[8] else [],
        "security": row[9],
        "suggestions": json.loads(row[10]) if row[10] else [],
        "optimized_code": row[11]
    }
