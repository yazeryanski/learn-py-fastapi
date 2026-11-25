from fastapi import APIRouter, HTTPException, Query
from typing import Annotated

from src.services.students_service import StudentsService
from src.models.students_model import StudentCreate, StudentsFilter, Student

router = APIRouter()
students_service = StudentsService()


@router.get("/")
def get_students(
    filters: Annotated[StudentsFilter, Query()]
) -> list[Student]:
    students = students_service.get_students(filters)

    if not students:
        raise HTTPException(
            status_code=404, detail="No students found. Try adjusting your search criteria.")

    return students


@router.get("/{student_id}")
def get_single_student(student_id: int) -> Student:
    student = students_service.get_student_by_id(student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@router.post("/", status_code=201)
def add_student(student: StudentCreate) -> Student:
    added_student = students_service.add_student(student)
    return added_student


@router.delete("/{student_id}")
def remove_student(student_id: int) -> bool:
    success = students_service.remove_student(student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return success
