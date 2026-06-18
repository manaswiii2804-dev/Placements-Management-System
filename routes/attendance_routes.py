from fastapi import APIRouter, HTTPException
from database import supabase

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@router.post("/")
def create_attendance(
    student_id: int,
    attendance_date: str,
    status: str
):

    if status not in ["Present", "Absent"]:
        raise HTTPException(
            status_code=400,
            detail="Status must be Present or Absent"
        )

    result = (
        supabase.table("attendance")
        .insert({
            "student_id": student_id,
            "attendance_date": attendance_date,
            "status": status
        })
        .execute()
    )

    return result.data


@router.get("/")
def get_all_attendance():

    result = (
        supabase.table("attendance")
        .select("*")
        .execute()
    )

    return result.data


@router.get("/{attendance_id}")
def get_attendance(attendance_id: int):

    result = (
        supabase.table("attendance")
        .select("*")
        .eq("id", attendance_id)
        .execute()
    )

    if not result.data:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    return result.data[0]


@router.put("/{attendance_id}")
def update_attendance(
    attendance_id: int,
    status: str
):

    if status not in ["Present", "Absent"]:
        raise HTTPException(
            status_code=400,
            detail="Status must be Present or Absent"
        )

    result = (
        supabase.table("attendance")
        .update({
            "status": status
        })
        .eq("id", attendance_id)
        .execute()
    )

    return result.data


@router.delete("/{attendance_id}")
def delete_attendance(attendance_id: int):

    (
        supabase.table("attendance")
        .delete()
        .eq("id", attendance_id)
        .execute()
    )

    return {
        "message": "Attendance deleted successfully"
    }