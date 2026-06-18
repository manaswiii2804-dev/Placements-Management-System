from fastapi import APIRouter, HTTPException
from database import supabase
from utils.password_hashing import hash_password, verify_password
from utils.jwt_handler import create_token

router = APIRouter(prefix="/auth", tags=["Auth"])

VALID_ROLES = ["admin", "trainer", "student"]


@router.post("/register")
def register(email: str, password: str, role: str):

    if role not in VALID_ROLES:
        raise HTTPException(
            status_code=400,
            detail="Invalid role"
        )

    existing_user = (
        supabase.table("users")
        .select("*")
        .eq("email", email)
        .execute()
    )

    if existing_user.data:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = hash_password(password)

    result = (
        supabase.table("users")
        .insert({
            "email": email,
            "password": hashed_password,
            "role": role
        })
        .execute()
    )

    return {
        "message": "User registered successfully",
        "user": result.data[0]
    }


@router.post("/login")
def login(email: str, password: str):

    result = (
        supabase.table("users")
        .select("*")
        .eq("email", email)
        .execute()
    )

    if not result.data:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user = result.data[0]

    if not verify_password(
        password,
        user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_token({
        "user_id": user["id"],
        "role": user["role"]
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user["role"]
    }