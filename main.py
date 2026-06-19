from fastapi import FastAPI
from routes import (
    auth_routes,
    student_routes,
    attendance_routes,
    placement_routes,
    assessment_routes,
    result_routes,
    feedback_routes,
    placement_record_routes
)

app = FastAPI(title="Placement Management System")

app.include_router(auth_routes.router)
app.include_router(student_routes.router)
app.include_router(attendance_routes.router)
app.include_router(placement_routes.router)
app.include_router(assessment_routes.router)
app.include_router(result_routes.router)
app.include_router(feedback_routes.router)
app.include_router(placement_record_routes.router)


@app.get("/")
def home():
    return {"message": "System Running Successfully"}