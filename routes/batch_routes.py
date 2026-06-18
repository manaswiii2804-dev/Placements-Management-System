from fastapi import APIRouter
from database import supabase

router = APIRouter(prefix="/batches", tags=["Batches"])

@router.post("/")
def create_batch(batch: dict):
    return supabase.table("training_batches").insert(batch).execute().data

@router.get("/")
def get_batches():
    return supabase.table("training_batches").select("*").execute().data