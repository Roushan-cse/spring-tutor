from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.ChatRequest import ChatRequest
from app.models.ChatResponse import ChatResponse
from app.services.RagService import RagService

router = APIRouter(
    prefix="/api/chat",
    tags=["Chat"]
)

rag_service = RagService()


@router.post("/ask", response_model=ChatResponse)
def ask_question(request: ChatRequest):
    answer = rag_service.ask(
        request.question
    )

    return ChatResponse(
        answer=answer
    )


@router.post("/stream")
def stream_question(request: ChatRequest):

    return StreamingResponse(
        rag_service.stream(
            request.question
        ),
        media_type="text/plain"
    )