def get_review_prompt(code: str, filename: str) -> str:
    return f"""
You are a senior software engineer performing a code review.

Review the following code from file: {filename}

Code:
{code}

Provide your review in the following JSON format only. No extra text, no markdown.

{{
    "score": <overall score out of 10, multiplied by 10 to get 0-100>,
    "readability": <score out of 10>,
    "accuracy": <score out of 10>,
    "best_practices": <score out of 10>,
    "bugs": [<list of bug descriptions as strings, empty list if none>],
    "security": "<Good | Moderate | Poor>",
    "suggestions": [<list of improvement suggestions as strings>],
    "optimized_code": "<the improved version of the code>"
}}
"""
