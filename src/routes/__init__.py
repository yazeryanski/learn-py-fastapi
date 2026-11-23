from .students_router import router as students_router
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1")

router.include_router(students_router, prefix="/students")