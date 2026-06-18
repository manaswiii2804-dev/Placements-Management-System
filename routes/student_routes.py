from fastapi import APIRouter, HTTPException
from database import supabase

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post("/")
def create_student(
    user_id: int,
    full_name: str,
    college_id: int = None,
    batch_id: int = None,
    branch: str = None,
    year: int = None,
    cgpa: float = None,
    phone: str = None
):

    existing = (
        supabase.table("students")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )

    if existing.data:
        raise HTTPException(
            status_code=400,
            detail="Student already exists"
        )

    result = (
        supabase.table("students")
        .insert({
            "user_id": user_id,
            "full_name": full_name,
            "college_id": college_id,
            "batch_id": batch_id,
            "branch": branch,
            "year": year,
            "cgpa": cgpa,
            "phone": phone
        })
        .execute()
    )

    return result.data


@router.get("/")
def get_all_students():

    result = (
        supabase.table("students")
        .select("*")
        .execute()
    )

    return result.data


@router.get("/{student_id}")
def get_student(student_id: int):

    result = (
        supabase.table("students")
        .select("*")
        .eq("id", student_id)
        .execute()
    )

    if not result.data:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return result.data[0]


@router.put("/{student_id}")
def update_student(
    student_id: int,
    full_name: str = None,
    branch: str = None,
    year: int = None,
    cgpa: float = None,
    phone: str = None,
    placement_status: str = None
):

    update_data = {}

    if full_name is not None:
        update_data["full_name"] = full_name

    if branch is not None:
        update_data["branch"] = branch

    if year is not None:
        update_data["year"] = year

    if cgpa is not None:
        update_data["cgpa"] = cgpa

    if phone is not None:
        update_data["phone"] = phone

    if placement_status is not None:
        update_data["placement_status"] = placement_status

    result = (
        supabase.table("students")
        .update(update_data)
        .eq("id", student_id)
        .execute()
    )

    return result.data


@router.delete("/{student_id}")
def delete_student(student_id: int):

    (
        supabase.table("students")
        .delete()
        .eq("id", student_id)
        .execute()
    )

    return {
        "message": "Student deleted successfully"
    }