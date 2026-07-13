import anthropic

from src.services.ai.base import AIService
from src.config import settings
from src.utils.prompts import get_review_prompt
from src.utils.helpers import parse_ai_response


class AnthropicService(AIService):

    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=settings.ANTHROPIC_API_KEY
        )

    def review_code(self, code: str, filename: str) -> dict:

        prompt = get_review_prompt(code, filename)

        response = self.client.messages.create(
            model="claude-sonnet-4-0",
            max_tokens=4000,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return parse_ai_response(
            response.content[0].text
        )