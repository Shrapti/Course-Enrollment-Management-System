from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import List

# --- Student Schemas ---
class StudentBase(BaseModel):
    name: str
    email: str

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    class Config:
        from_attributes = True

# --- Course Schemas ---
class CourseBase(BaseModel):
    title: str
    instructor: str
    capacity: int = Field(..., gt=0, description="Capacity must be a positive integer")
    fee: float = Field(..., ge=0)

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int
    seats_available: int
    class Config:
        from_attributes = True

# --- Enrollment Schemas ---
class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int
    enrollment_date: date
    status: str
    class Config:
        from_attributes = True
