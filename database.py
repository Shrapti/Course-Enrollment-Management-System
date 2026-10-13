from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./course_enrollment.db"

engine = create_engine(
    # connect_args needed only for SQLite to handle multi-threading safely
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to inject DB session into path operations
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
