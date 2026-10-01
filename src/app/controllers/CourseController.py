from fastapi import APIRouter


router = APIRouter(
    prefix = "/api/courses",
    tags=["Courses"]
)

@router.get("/")
def get_courses():
    return []


@router.get("/{course_id}")
def get_course(course_id : int):
    return {
        "id":course_id
    }

@router.get("/{course_id}/lectures")
def get_lectures(course_id : int):
    return []



