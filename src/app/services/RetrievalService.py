from pinecone import Pinecone

from langchain_ollama import OllamaEmbeddings

from app.config.settings import (
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME
)


class RetrievalService:

    def __init__(self):

        self.embeddings = OllamaEmbeddings(
            model="nomic-embed-text:latest"
        )

        pc = Pinecone(
            api_key=PINECONE_API_KEY
        )

        self.index = pc.Index(
            PINECONE_INDEX_NAME
        )

    def retrieve(self, question: str):

        query_vector = self.embeddings.embed_query(
            question
        )

        result = self.index.query(
            vector=query_vector,
            top_k=5,
            include_metadata=True
        )

        documents = []

        for match in result.matches:

            text = match.metadata.get(
                "text",
                ""
            )

            if text:
                documents.append(text)

        return documents