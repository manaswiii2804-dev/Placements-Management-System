from fastapi import FastAPI
from routes import (
    auth_routes,
    college_routes,
    trainer_routes,
    batch_routes,
    student_routes,
    attendance_routes,
    assessment_routes,
    result_routes,
    placement_routes,
    application_routes,
    feedback_routes,
    placement_record_routes
)

app = FastAPI(title="Student Placement System")

app.include_router(auth_routes.router)
app.include_router(college_routes.router)
app.include_router(trainer_routes.router)
app.include_router(batch_routes.router)
app.include_router(student_routes.router)
app.include_router(attendance_routes.router)
app.include_router(assessment_routes.router)
app.include_router(result_routes.router)
app.include_router(placement_routes.router)
app.include_router(application_routes.router)
app.include_router(feedback_routes.router)
app.include_router(placement_record_routes.router)

@app.get("/")
def home():
    return {"message": "Placement System Backend Running"}