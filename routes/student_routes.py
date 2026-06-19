from fastapi import APIRouter, HTTPException
from database import supabase

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/")
def create_student(user_id: int, full_name: str, branch: str = None, year: int = None, cgpa: float = None, phone: str = None):

    exists = supabase.table("students").select("*").eq("user_id", user_id).execute()

    if exists.data:
        raise HTTPException(400, "Student exists")

    return supabase.table("students").insert({
        "user_id": user_id,
        "full_name": full_name,
        "branch": branch,
        "year": year,
        "cgpa": cgpa,
        "phone": phone,
        "placement_status": "Not Placed"
    }).execute().data


@router.get("/")
def get_students():
    return supabase.table("students").select("*").execute().data