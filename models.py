from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    enrollments = relationship("Enrollment", back_populates="student")

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    instructor = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    seats_available = Column(Integer, nullable=False)
    fee = Column(Float, nullable=False)

    enrollments = relationship("Enrollment", back_populates="course")

class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    enrollment_date = Column(Date, nullable=False)
    status = Column(String, default="active", nullable=False) # "active" or "cancelled"

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
