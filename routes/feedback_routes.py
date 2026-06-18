from fastapi import APIRouter
from database import supabase

router = APIRouter(prefix="/feedback", tags=["Interview Feedback"])

@router.post("/")
def add_feedback(data: dict):
    return supabase.table("interview_feedback").insert(data).execute().data

@router.get("/")
def get_feedback():
    return supabase.table("interview_feedback").select("*").execute().data