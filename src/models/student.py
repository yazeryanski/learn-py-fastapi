from pydantic import BaseModel, Field, ConfigDict, computed_field
from datetime import datetime
from enum import StrEnum


class Department(StrEnum):
    SCIENCE = "Science"
    ARTS = "Arts"
    COMMERCE = "Commerce"
    ENGINEERING = "Engineering"
    MEDICINE = "Medicine"


class Student(BaseModel):
    id: int
    name: str = Field(..., max_length=15)
    surname: str = Field(..., max_length=30)

    @computed_field
    @property
    def full_name(self) -> str:
        return f"{self.name} {self.surname}"

    department: Department
    age: int | None = Field(ge=0, le=150, default=None)
    grade: int | None = Field(ge=1, le=20, default=None)
    absences: int | None = Field(ge=0, le=100, default=None)

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    # Config class
    model_config = ConfigDict({
        'json_encoders': {
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S")
        }
    })
