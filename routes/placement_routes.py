from fastapi import APIRouter
from database import supabase

router = APIRouter(prefix="/placements", tags=["Placements"])

@router.post("/drives")
def create_drive(data: dict):
    return supabase.table("placement_drives").insert(data).execute().data

@router.get("/drives")
def get_drives():
    return supabase.table("placement_drives").select("*").execute().data