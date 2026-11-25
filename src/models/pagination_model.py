from pydantic import BaseModel, Field


class PaginationFilter(BaseModel):
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
