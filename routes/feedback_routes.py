from fastapi import APIRouter
from database import supabase

router = APIRouter(prefix="/feedback", tags=["Feedback"])


@router.post("/")
def add_feedback(drive_id: int, student_id: int, feedback: str, rating: int):

    return supabase.table("interview_feedback").insert({
        "drive_id": drive_id,
        "student_id": student_id,
        "feedback": feedback,
        "rating": rating
    }).execute().data


@router.get("/")
def get_feedback():
    return supabase.table("interview_feedback").select("*").execute().data