import streamlit as st
import requests

# --- API BACKEND SETUP ---
BASE_URL = "http://127.0.0.1:8000" 

# --- UI HEADER ---
st.set_page_config(layout="wide")
st.title("🎓 Online Course Enrollment Management System")

# --- NAVIGATION TABS ---
tab1, tab2, tab3 = st.tabs(["📚 Courses Management", "👤 Students Management", "📝 Enrollments"])

# ==========================================
# TAB 1: COURSES MANAGEMENT
# ==========================================
with tab1:
    st.header("Course Administration")
    # Fixed: Explicitly passing 2 to create two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Add New Course")
        c_title = st.text_input("Course Title")
        c_instructor = st.text_input("Instructor Name")
        c_capacity = st.number_input("Seat Capacity", min_value=1, value=30)
        c_fee = st.number_input("Course Fee ($)", min_value=0.0, value=0.00, step=10.0)
        
        if st.button("Create Course"):
            if c_title and c_instructor:
                payload = {
                    "title": c_title,
                    "instructor": c_instructor,
                    "capacity": int(c_capacity),
                    "fee": float(c_fee)
                }
                try:
                    response = requests.post(f"{BASE_URL}/courses", json=payload)
                    if response.status_code == 200 or response.status_code == 201:
                        st.success(f"Course '{c_title}' saved to backend successfully!")
                        st.rerun()
                    else:
                        st.error(f"Backend rejected data ({response.status_code}): {response.text}")
                except requests.exceptions.ConnectionError:
                    st.error("Could not connect to the backend. Is your API server running?")
            else:
                st.error("Please fill out Title and Instructor fields.")

    with col2:
        st.subheader("Available Courses List")
        if st.button("Refresh Courses"):
            st.rerun()
        
        try:
            response = requests.get(f"{BASE_URL}/courses")
            if response.status_code == 200:
                courses = response.json()
                if courses:
                    for item in courses:
                        st.markdown(f"**[{item.get('id')}] {item.get('title')}** by {item.get('instructor')}  \n"
                                    f"🪑 Seats: {item.get('available', item.get('capacity'))}/{item.get('capacity')} | 💵 Fee: ${float(item.get('fee', 0)):.2f}")
                        st.divider()
                else:
                    st.info("No courses available yet.")
            else:
                st.error("Failed to retrieve courses from the API backend.")
        except requests.exceptions.ConnectionError:
            st.info("Ensure your backend is running to see available courses.")

# ==========================================
# TAB 2: STUDENTS MANAGEMENT
# ==========================================
with tab2:
    st.header("Student Administration")
    # Fixed: Explicitly passing 2 to create two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Register New Student")
        s_name = st.text_input("Student Full Name")
        s_email = st.text_input("Email Address")
        
        if st.button("Register Student"):
            if s_name and s_email:
                payload = {"name": s_name, "email": s_email}
                try:
                    response = requests.post(f"{BASE_URL}/students", json=payload)
                    if response.status_code == 200 or response.status_code == 201:
                        st.success(f"Student '{s_name}' registered to backend successfully!")
                        st.rerun()
                    else:
                        st.error(f"Backend rejected registration: {response.text}")
                except requests.exceptions.ConnectionError:
                    st.error("Backend server is unreachable.")
            else:
                st.error("Please fill out Name and Email fields.")

    with col2:
        st.subheader("Registered Students List")
        try:
            response = requests.get(f"{BASE_URL}/students")
            if response.status_code == 200:
                students = response.json()
                if students:
                    for item in students:
                        st.markdown(f"**ID: {item.get('id')}** | Name: {item.get('name')}  \n📧 Email: {item.get('email')}")
                        st.divider()
                else:
                    st.info("No students registered yet.")
        except requests.exceptions.ConnectionError:
            st.info("Ensure backend is running to list students.")

# ==========================================
# TAB 3: ENROLLMENTS
# ==========================================
with tab3:
    st.header("Course Enrollment Management")
    
    try:
        res_students = requests.get(f"{BASE_URL}/students")
        res_courses = requests.get(f"{BASE_URL}/courses")
        
        if res_students.status_code == 200 and res_courses.status_code == 200:
            db_students = res_students.json()
            db_courses = [c for c in res_courses.json() if c.get('available', 1) > 0]
            
            if not db_students or not db_courses:
                st.warning("You need at least one registered student and one active course to manage enrollments.")
            else:
                # Fixed: Explicitly passing 2 to create two columns
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Enroll Student in Course")
                    student_options = {f"{item.get('name')} (ID: {item.get('id')})": item.get('id') for item in db_students}
                    course_options = {f"{item.get('title')} ({item.get('available')} seats left)": item.get('id') for item in db_courses}
                    
                    selected_student = st.selectbox("Select Student", list(student_options.keys()))
                    selected_course = st.selectbox("Select Course", list(course_options.keys()))
                    
                    if st.button("Confirm Enrollment"):
                        s_id = student_options[selected_student]
                        c_id = course_options[selected_course]
                        
                        payload = {"student_id": s_id, "course_id": c_id}
                        enroll_res = requests.post(f"{BASE_URL}/enrollments", json=payload)
                        
                        if enroll_res.status_code == 200 or enroll_res.status_code == 201:
                            st.success("Enrollment processed on backend!")
                            st.rerun()
                        else:
                            st.error(f"Backend rejected enrollment: {enroll_res.text}")
                            
                with col2:
                    st.subheader("Active Enrollment Records")
                    res_enroll = requests.get(f"{BASE_URL}/enrollments")
                    if res_enroll.status_code == 200:
                        enrollments = res_enroll.json()
                        if enrollments:
                            for item in enrollments:
                                st.markdown(f"📝 **Record #{item.get('id')}**: Student ID {item.get('student_id')} ➡️ Course ID {item.get('course_id')}")
                                st.divider()
                        else:
                            st.info("No enrollment transactions recorded yet.")
    except requests.exceptions.ConnectionError:
        st.info("Ensure your API server is active to use the enrollment module.")
