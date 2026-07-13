from abc import ABC, abstractmethod


class AIService(ABC):

    @abstractmethod
    def review_code(self, code: str, filename: str) -> dict:
        """
        Review the given source code and return
        a parsed dictionary containing the review.
        """
        pass