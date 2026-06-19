from fastapi import APIRouter
from database import supabase

router = APIRouter(prefix="/results", tags=["Results"])


@router.post("/")
def add_result(assessment_id: int, student_id: int, marks_obtained: int):

    return supabase.table("assessment_results").insert({
        "assessment_id": assessment_id,
        "student_id": student_id,
        "marks_obtained": marks_obtained
    }).execute().data


@router.get("/")
def get_results():
    return supabase.table("assessment_results").select("*").execute().data