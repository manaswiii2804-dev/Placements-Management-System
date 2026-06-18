from fastapi import APIRouter
from database import supabase

router = APIRouter(prefix="/assessments", tags=["Assessments"])

@router.post("/")
def create_assessment(data: dict):
    return supabase.table("assessments").insert(data).execute().data

@router.get("/")
def get_assessments():
    return supabase.table("assessments").select("*").execute().data