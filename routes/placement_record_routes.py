from fastapi import APIRouter
from database import supabase

router = APIRouter(prefix="/placement-records", tags=["Placement Records"])


@router.post("/")
def add_record(student_id: int, company_name: str, job_role: str, package: float, joining_date: str):

    return supabase.table("placement_records").insert({
        "student_id": student_id,
        "company_name": company_name,
        "job_role": job_role,
        "package": package,
        "joining_date": joining_date
    }).execute().data


@router.get("/")
def get_records():
    return supabase.table("placement_records").select("*").execute().data