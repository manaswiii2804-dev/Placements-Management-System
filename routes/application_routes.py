from fastapi import APIRouter
from database import supabase

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.post("/")
def apply(data: dict):
    return supabase.table("drive_applications").insert(data).execute().data

@router.get("/")
def get_applications():
    return supabase.table("drive_applications").select("*").execute().data