from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import engine, Base, get_db
import models, schemas, crud

# Generate DB schema tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Online Course Enrollment API")

# ==========================================
# COURSES ROUTING
# ==========================================

@app.get("/courses", response_model=List[schemas.CourseResponse], tags=["Courses"])
def read_courses(db: Session = Depends(get_db)):
    return crud.get_courses(db)

@app.get("/courses/{id}", response_model=schemas.CourseResponse, tags=["Courses"])
def read_course(id: int, db: Session = Depends(get_db)):
    course = crud.get_course(db, course_id=id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.post("/courses", response_model=schemas.CourseResponse, status_code=201, tags=["Courses"])
def add_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, course)

@app.put("/courses/{id}", response_model=schemas.CourseResponse, tags=["Courses"])
def update_existing_course(id: int, course: schemas.CourseCreate, db: Session = Depends(get_db)):
    updated_course = crud.update_course(db, course_id=id, course_data=course)
    if not updated_course:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated_course

@app.delete("/courses/{id}", tags=["Courses"])
def remove_course(id: int, db: Session = Depends(get_db)):
    success = crud.delete_course(db, course_id=id)
    if not success:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"detail": "Course removed successfully"}

# ==========================================
# STUDENTS ROUTING
# ==========================================

@app.get("/students", response_model=List[schemas.StudentResponse], tags=["Students"])
def read_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

@app.get("/students/{id}", response_model=schemas.StudentResponse, tags=["Students"])
def read_student(id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id=id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/students", response_model=schemas.StudentResponse, status_code=201, tags=["Students"])
def register_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.put("/students/{id}", response_model=schemas.StudentResponse, tags=["Students"])
def update_existing_student(id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    updated_student = crud.update_student(db, student_id=id, student_data=student)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@app.delete("/students/{id}", tags=["Students"])
def remove_student(id: int, db: Session = Depends(get_db)):
    success = crud.delete_student(db, student_id=id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student removed successfully"}

# ==========================================
# ENROLLMENTS ROUTING
# ==========================================

@app.post("/enroll", response_model=schemas.EnrollmentResponse, status_code=201, tags=["Enrollments"])
def enroll_student(enrollment: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    return crud.create_enrollment(db, enrollment)

@app.get("/enrollments/student/{id}", response_model=List[schemas.EnrollmentResponse], tags=["Enrollments"])
def read_student_enrollments(id: int, db: Session = Depends(get_db)):
    return crud.get_enrollments_by_student(db, student_id=id)

@app.get("/enrollments/course/{id}", response_model=List[schemas.EnrollmentResponse], tags=["Enrollments"])
def read_course_enrollments(id: int, db: Session = Depends(get_db)):
    return crud.get_enrollments_by_course(db, course_id=id)

@app.delete("/enrollments/{id}", tags=["Enrollments"])
def cancel_enrollment(id: int, db: Session = Depends(get_db)):
    success = crud.delete_enrollment(db, enrollment_id=id)
    if not success:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return {"detail": "Enrollment cancelled successfully"}
