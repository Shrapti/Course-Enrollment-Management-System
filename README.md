# 🎓 Course Enrollment Management System

## 📌 Project Overview

The Course Enrollment Management System is a Python-based application
developed to manage courses, student registrations, and course enrollments.

The project uses FastAPI to handle backend API operations, Streamlit
to provide an interactive user interface, and SQLite to store data.

It simplifies course administration and helps manage student enrollment
records through a user-friendly application.

## 🎯 Project Objectives

- Manage courses and instructor details.
- Register students and maintain their information.
- Enroll students in available courses.
- Track course seat capacity and fees.
- Store and retrieve records from the database.
- Connect the frontend with the backend through REST APIs.

## 🛠️ Technologies Used

- Python
- FastAPI
- Streamlit
- SQLite
- SQLAlchemy
- REST API
- Requests
- Swagger UI / OpenAPI

## ✨ Key Features

### 📚 Course Management
- Add new courses.
- Store course titles and instructor names.
- Set course capacity and fees.
- View available courses and seat information.

### 👤 Student Management
- Register new students.
- Store student names and email addresses.
- View registered student records.

### 📝 Enrollment Management
- Select students and available courses.
- Process course enrollment requests.
- View enrollment records.
- Track course seat availability.

### 🗄️ Database Management
- SQLite database integration.
- SQLAlchemy ORM for database operations.
- Persistent storage of application records.

## 🏗️ Project Architecture

The application consists of three main components:

1. **Frontend:** Streamlit provides the user interface.
2. **Backend:** FastAPI handles API requests and application logic.
3. **Database:** SQLite stores courses, students, and enrollment records.

The frontend sends HTTP requests to the backend API.
The backend processes requests and interacts with the database.

## 📂 Project Structure

Course-Enrollment-Management-System/
│
├── app.py
├── crud.py
├── database.py
├── course_enrollment.db
├── main.py
├── models.py
├── schemas.py
├── requirements.txt
└── README.md

Note: Add main.py, models.py, schemas.py, and requirements.txt
if they are part of your project. These files were not included
in the uploaded files.

## 🚀 How to Run the Project

### 1. Clone the Repository

git clone <your-github-repository-url>

### 2. Navigate to the Project Folder

cd Course-Enrollment-Management-System

### 3. Install Dependencies

pip install fastapi uvicorn streamlit requests sqlalchemy

### 4. Start the FastAPI Backend

uvicorn main:app --reload

### 5. Open the API Documentation

Visit:

http://127.0.0.1:8000/docs

### 6. Run the Streamlit Frontend

Open another terminal and run:

streamlit run app.py

The application will open in your browser.

## 📈 Learning Outcomes

- Understanding REST API development using FastAPI.
- Building interactive interfaces with Streamlit.
- Performing database operations using SQLite and SQLAlchemy.
- Implementing CRUD operations.
- Connecting frontend applications with backend APIs.
- Managing relationships between application entities.

## 👩‍💻 Author

Shrapti Bedre

Aspiring Data Analyst | Python | SQL | Power BI
