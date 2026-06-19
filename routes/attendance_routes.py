from fastapi import APIRouter, HTTPException
from database import supabase

router = APIRouter(prefix="/attendance", tags=["Attendance"])


@router.post("/")
def mark(student_id: int, attendance_date: str, status: str):

    if status not in ["Present", "Absent"]:
        raise HTTPException(400, "Invalid status")

    return supabase.table("attendance").insert({
        "student_id": student_id,
        "attendance_date": attendance_date,
        "status": status
    }).execute().data


@router.get("/")
def get_all():
    return supabase.table("attendance").select("*").execute().data