from pydantic import BaseModel, Field, ConfigDict, computed_field
from datetime import datetime
from enum import StrEnum

from src.models.pagination_model import PaginationFilter


class Department(StrEnum):
    SCIENCE = "Science"
    ARTS = "Arts"
    COMMERCE = "Commerce"
    ENGINEERING = "Engineering"
    MEDICINE = "Medicine"


class StudentBase(BaseModel):
    name: str = Field(..., max_length=15)
    surname: str = Field(..., max_length=30)
    department: Department
    age: int | None = Field(ge=0, le=150, default=None)
    grade: int | None = Field(ge=1, le=20, default=None)
    absences: int | None = Field(ge=0, le=100, default=None)

    model_config = ConfigDict({
        "extra": "forbid"
    })


class StudentCreate(StudentBase):
    """POST body: no id, no timestamps."""
    pass


class Student(StudentBase):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @computed_field
    @property
    def full_name(self) -> str:
        return f"{self.name} {self.surname}"


class StudentsFilter(PaginationFilter):
    department: Department | None = None
    search: str | None = Field(
        None,
        max_length=50,
        description="Search term for filtering students"
    )
