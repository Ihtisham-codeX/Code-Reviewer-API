import google.generativeai as genai
from src.config import settings
from src.utils.prompts import get_review_prompt
from src.utils.helpers import parse_ai_response

# Configure Gemini with API key
genai.configure(api_key=settings.GEMINI_API_KEY)

# Load the model once
model = genai.GenerativeModel("gemini-1.5-flash")


def review_code(code: str, filename: str) -> dict:
    # Build the prompt
    prompt = get_review_prompt(code, filename)

    # Send to Gemini
    response = model.generate_content(prompt)

    # Parse and return the JSON result
    result = parse_ai_response(response.text)

    return result
