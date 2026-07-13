from openai import OpenAI

from src.services.ai.base import AIService
from src.config import settings
from src.utils.prompts import get_review_prompt
from src.utils.helpers import parse_ai_response


class OpenAIService(AIService):

    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def review_code(self, code: str, filename: str) -> dict:

        prompt = get_review_prompt(code, filename)

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return parse_ai_response(
            response.choices[0].message.content
        )