from fastapi import APIRouter
from database import supabase

router = APIRouter(prefix="/results", tags=["Assessment Results"])

@router.post("/")
def add_result(data: dict):
    return supabase.table("assessment_results").insert(data).execute().data

@router.get("/")
def get_results():
    return supabase.table("assessment_results").select("*").execute().data