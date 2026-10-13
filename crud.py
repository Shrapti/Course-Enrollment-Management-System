from sqlalchemy.orm import Session
import models, schemas

# ==========================================
# 1. COURSES CRUD OPERATIONS
# ==========================================

def get_courses(db: Session):
    return db.query(models.Course).all()

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def create_course(db: Session, course: schemas.CourseCreate):
    # Unpack properties and explicitly declare initial seats available
    db_course = models.Course(
        title=course.title,
        instructor=course.instructor,
        capacity=course.capacity,
        fee=course.fee,
        seats_available=course.capacity  # <-- FIX: Sets initial available seats to equal the capacity
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def update_course(db: Session, course_id: int, course_data: schemas.CourseCreate):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if db_course:
        for key, value in course_data.dict().items():
            setattr(db_course, key, value)
        db.commit()
        db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if db_course:
        db.delete(db_course)
        db.commit()
        return True
    return False

# ==========================================
# 2. STUDENTS CRUD OPERATIONS
# ==========================================

def get_students(db: Session):
    return db.query(models.Student).all()

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, student_data: schemas.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        for key, value in student_data.dict().items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
        return True
    return False

# ==========================================
# 3. ENROLLMENTS CRUD OPERATIONS
# ==========================================

def create_enrollment(db: Session, enrollment: schemas.EnrollmentCreate):
    db_enrollment = models.Enrollment(**enrollment.dict())
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment

def get_enrollments_by_student(db: Session, student_id: int):
    return db.query(models.Enrollment).filter(models.Enrollment.student_id == student_id).all()

def get_enrollments_by_course(db: Session, course_id: int):
    return db.query(models.Enrollment).filter(models.Enrollment.course_id == course_id).all()

def delete_enrollment(db: Session, enrollment_id: int):
    db_enrollment = db.query(models.Enrollment).filter(models.Enrollment.id == enrollment_id).first()
    if db_enrollment:
        db.delete(db_enrollment)
        db.commit()
        return True
    return False
