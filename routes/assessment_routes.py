from fastapi import APIRouter, HTTPException
from database import supabase

router = APIRouter(prefix="/assessments", tags=["Assessments"])


@router.post("/")
def create_assessment(title: str, description: str = None, max_marks: int = 100):

    return supabase.table("assessments").insert({
        "title": title,
        "description": description,
        "max_marks": max_marks
    }).execute().data


@router.get("/")
def get_all_assessments():
    return supabase.table("assessments").select("*").execute().data


@router.get("/{assessment_id}")
def get_assessment(assessment_id: int):

    data = supabase.table("assessments").select("*").eq("id", assessment_id).execute().data

    if not data:
        raise HTTPException(404, "Assessment not found")

    return data[0]


@router.delete("/{assessment_id}")
def delete_assessment(assessment_id: int):

    supabase.table("assessments").delete().eq("id", assessment_id).execute()

    return {"message": "Assessment deleted"}