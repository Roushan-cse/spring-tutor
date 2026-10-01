from langchain_openai import ChatOpenAI

from app.config.settings import HF_TOKEN


class LLMService:

    def __init__(self):

        self.llm = ChatOpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=HF_TOKEN,
            model="openai/gpt-oss-120b"
        )

    def generate(self, prompt: str):

        response = self.llm.invoke(
            prompt
        )

        return response.content

    def stream(self, prompt: str):

        for chunk in self.llm.stream(prompt):

            if chunk.content:

                yield chunk.content