from pinecone import Pinecone

pc = Pinecone(
    api_key="YOUR_PINECONE_API_KEY"
)

index = pc.Index("spring-tutor")