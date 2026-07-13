from src.services.ai.gemini_service import GeminiService
from src.services.ai.openai_service import OpenAIService
from src.services.ai.anthropic_service import AnthropicService
from src.utils.enums import AIProvider

class AIFactory:

    @staticmethod
    def get_ai(provider):

        if provider == AIProvider.OPENAI:
            return OpenAIService()

        elif provider == AIProvider.ANTHROPIC:
            return AnthropicService()

        return GeminiService()