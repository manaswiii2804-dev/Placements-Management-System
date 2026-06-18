from fastapi import APIRouter
from database import supabase

router = APIRouter(prefix="/placement-records", tags=["Placement Records"])

@router.post("/")
def add_record(data: dict):
    return supabase.table("placement_records").insert(data).execute().data

@router.get("/")
def get_records():
    return supabase.table("placement_records").select("*").execute().data