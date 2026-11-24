from fastapi import APIRouter, HTTPException, Query
from src.data import students, students_search_indexes
from src.models.student import Department, Student
from pydantic import BaseModel, Field
from typing import Annotated

router = APIRouter()


class GetStudentsFilter(BaseModel):
    department: Department | None = None
    search: str | None = Field(
        None,
        max_length=50,
        description="Search term for filtering students"
    )
    limit: int = Field(
        20,
        ge=1,
        le=100,
        description="Maximum number of students to return"
    )
    offset: int = Field(
        0,
        ge=0,
        description="Number of students to skip"
    )


@router.get("/")
def get_students(
    filters: Annotated[GetStudentsFilter, Query()]
) -> list[Student]:
    filtered_students = students

    if filters.search is not None:
        filters.search = filters.search.lower()
        # TODO: Make it readable and efficient
        filtered_students = [st for st in filtered_students if students_search_indexes.get(
            st.id, "").find(filters.search) != -1]

    if filters.department is not None:
        filtered_students = [s for s in filtered_students if s.department == filters.department]

    if not filtered_students:
        raise HTTPException(
            status_code=404, detail="No students found. Try adjusting your search criteria.")

    return filtered_students[filters.offset:filters.offset + filters.limit]


@router.get("/{student_id}")
def get_single_student(student_id: int) -> Student:
    student = next((s for s in students if s.id == student_id), None)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student
