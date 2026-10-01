from app.services.RetrievalService import RetrievalService
from app.services.PromptService import PromptService
from app.services.LLMService import LLMService


class RagService:

    def __init__(self):
        self.retrieval_service = RetrievalService()
        self.prompt_service = PromptService()
        self.llm_service = LLMService()

    def ask(self, question: str):
        docs = self.retrieval_service.retrieve(
            question
        )

        prompt = self.prompt_service.build_prompt(
            question=question,
            documents=docs
        )

        answer = self.llm_service.generate(
            prompt
        )

        return answer

    def stream(self, question: str):
        docs = self.retrieval_service.retrieve(
            question
        )

        prompt = self.prompt_service.build_prompt(
            question=question,
            documents=docs
        )

        for chunk in self.llm_service.stream(prompt):
            yield chunk