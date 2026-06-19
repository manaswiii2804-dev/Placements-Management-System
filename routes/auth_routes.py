from fastapi import APIRouter, HTTPException
from database import supabase
from utils.jwt_handler import create_token
from utils.password_hashing import hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(email: str, password: str, role: str):

    exists = supabase.table("users").select("*").eq("email", email).execute()

    if exists.data:
        raise HTTPException(400, "User already exists")

    user = supabase.table("users").insert({
        "email": email,
        "password": hash_password(password),
        "role": role
    }).execute()

    return user.data


@router.post("/login")
def login(email: str, password: str):

    user = supabase.table("users").select("*").eq("email", email).execute()

    if not user.data:
        raise HTTPException(404, "User not found")

    user = user.data[0]

    if not verify_password(password, user["password"]):
        raise HTTPException(401, "Invalid password")

    token = create_token({"user_id": user["id"], "role": user["role"]})

    return {"access_token": token}