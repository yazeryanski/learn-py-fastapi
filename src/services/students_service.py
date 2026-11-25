from pydantic import BaseModel
from src.models.students_model import Student, StudentCreate, StudentsFilter

from src.data import students, students_search_indexes
from src.utils.unique_id import get_unique_id


class StudentsService(BaseModel):
    def get_students(self, filters: StudentsFilter) -> list[Student]:
        filtered_students = students

        if filters.search is not None:
            search = filters.search.lower()
            filtered_students = [st for st in filtered_students if students_search_indexes.get(
                st.id, "").find(search) != -1]

        if filters.department is not None:
            filtered_students = [
                st for st in filtered_students if st.department == filters.department]

        return filtered_students[filters.offset:filters.offset + filters.limit]

    def get_student_by_id(self, student_id: int) -> Student | None:
        return next((s for s in students if s.id == student_id), None)

    def add_student(self, student: StudentCreate) -> Student:
        new_student = Student.model_validate({
            **student.model_dump(),
            "id": get_unique_id(),
        })

        students.append(new_student)

        students_search_indexes[new_student.id] = (
            f"{student.name} {student.surname} {student.age} "
            f"{student.grade} {student.absences} {student.department}"
        ).lower()
        return new_student
      
    def remove_student(self, student_id: int) -> bool:
        student = self.get_student_by_id(student_id)
        if student:
            students.remove(student)
            students_search_indexes.pop(student.id, None)
            return True
        return False
