from fastapi import APIRouter
from database import supabase

router = APIRouter(prefix="/placements", tags=["Placements"])


@router.post("/")
def create_drive(company_name: str, job_role: str, package: float, drive_date: str, eligibility_cgpa: float):

    return supabase.table("placement_drives").insert({
        "company_name": company_name,
        "job_role": job_role,
        "package": package,
        "drive_date": drive_date,
        "eligibility_cgpa": eligibility_cgpa
    }).execute().data


@router.get("/")
def get_drives():
    return supabase.table("placement_drives").select("*").execute().data