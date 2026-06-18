from fastapi import APIRouter
from database import supabase

router = APIRouter(prefix="/trainers", tags=["Trainers"])

@router.post("/")
def create_trainer(trainer: dict):
    return supabase.table("trainers").insert(trainer).execute().data

@router.get("/")
def get_trainers():
    return supabase.table("trainers").select("*").execute().data

@router.put("/{id}")
def update_trainer(id: int, trainer: dict):
    return supabase.table("trainers").update(trainer).eq("id", id).execute().data

@router.delete("/{id}")
def delete_trainer(id: int):
    return supabase.table("trainers").delete().eq("id", id).execute().data