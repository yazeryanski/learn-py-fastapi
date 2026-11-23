from fastapi import APIRouter, HTTPException
from src.data import students

router = APIRouter()

@router.get("/")
def get_students():
  return students

@router.get("/{student_id}")
def get_single_student(student_id: int):
  student = next((s for s in students if s.id == student_id), None)
  
  if student is None:
    raise HTTPException(status_code=404, detail="Student not found")
  
  return student
