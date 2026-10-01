from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.ChatController import router as chat_router
from app.controllers.CourseController import router as course_router
from app.controllers.HealthController import router as health_router

app = FastAPI(
    title="Spring Tutor API",
    description="AI-powered Spring Boot Tutor using RAG",
    version="1.0.0"
)

app.include_router(chat_router)
app.include_router(course_router)
app.include_router(health_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Spring Tutor API is running"
    }