from fastapi import APIRouter, HTTPException
from src.data import students
from src.models.student import Department, Student

router = APIRouter()


@router.get("/")
def get_students() -> list[Student]:
    return students


@router.get("/{student_id}")
def get_single_student(student_id: int) -> Student:
    student = next((s for s in students if s.id == student_id), None)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@router.get("/department/{department_name: Department}")
def get_students_by_department(department_name: Department) -> list[Student]:
    filtered_students = [
        s for s in students if s.department == department_name]

    if not filtered_students:
        raise HTTPException(
            status_code=404, detail="No students found in this department")
    
    return filtered_students
