from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

app = FastAPI(
    title="Placement Management System",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 🔥 CORS (important if you connect frontend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later replace with frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📌 Health check route (better than plain home)
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "System is running successfully 🚀"
    }

# 📌 Root route
@app.get("/")
def home():
    return {
        "message": "Placement Management System API",
        "docs": "/docs"
    }

# 📦 Routers
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(student_routes.router, prefix="/students", tags=["Students"])
app.include_router(attendance_routes.router, prefix="/attendance", tags=["Attendance"])
app.include_router(placement_routes.router, prefix="/placements", tags=["Placements"])
app.include_router(assessment_routes.router, prefix="/assessments", tags=["Assessments"])
app.include_router(result_routes.router, prefix="/results", tags=["Results"])
app.include_router(feedback_routes.router, prefix="/feedback", tags=["Feedback"])
app.include_router(placement_record_routes.router, prefix="/records", tags=["Placement Records"])