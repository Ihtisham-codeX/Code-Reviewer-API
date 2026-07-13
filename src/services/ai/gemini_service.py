import google.generativeai as genai

from src.services.ai.base import AIService
from src.config import settings
from src.utils.prompts import get_review_prompt
from src.utils.helpers import parse_ai_response

genai.configure(api_key=settings.GEMINI_API_KEY)


class GeminiService(AIService):

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-3.1-flash-lite")

    def review_code(self, code: str, filename: str) -> dict:

        prompt = get_review_prompt(code, filename)

        response = self.model.generate_content(prompt)

        return parse_ai_response(response.text)