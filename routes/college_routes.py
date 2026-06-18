from fastapi import APIRouter
from database import supabase

router = APIRouter(prefix="/colleges", tags=["Colleges"])

@router.post("/")
def create_college(college: dict):
    return supabase.table("colleges").insert(college).execute().data

@router.get("/")
def get_colleges():
    return supabase.table("colleges").select("*").execute().data

@router.put("/{id}")
def update_college(id: int, college: dict):
    return supabase.table("colleges").update(college).eq("id", id).execute().data

@router.delete("/{id}")
def delete_college(id: int):
    return supabase.table("colleges").delete().eq("id", id).execute().data