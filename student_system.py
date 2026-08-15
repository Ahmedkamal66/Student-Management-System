class Course:
    """A class representing a university course."""
    def __init__(self, name, credits, grade):
        self.name = name           # Course name
        self.credits = credits     # Number of credit hours
        self.grade = grade.upper() # Letter grade (A, B, C, D, F)

class Student:
    """A class representing a student, holding their data and enrolled courses."""
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = [] # List to store Course objects

    def enroll_course(self, course_name, credits, grade):
        """Method to add a new course to the student's record."""
        new_course = Course(course_name, credits, grade)
        self.courses.append(new_course)
        print(f"✅ Course '{course_name}' successfully enrolled for student {self.name}.")

    def calculate_gpa(self):
        """Method to calculate the Cumulative GPA based on points and credit hours."""
        # Dictionary to map letter grades to points
        grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        
        total_credits = 0
        total_points = 0.0

        for course in self.courses:
            total_credits += course.credits
            # Get the point value; if the grade is invalid, default to 0.0
            points = grade_points.get(course.grade, 0.0)
            total_points += points * course.credits

        if total_credits == 0:
            return 0.0 # Prevent ZeroDivisionError if no courses are enrolled
            
        gpa = total_points / total_credits
        return round(gpa, 2)

    def display_info(self):
        """Method to print the student's academic transcript."""
        print("-" * 40)
        print(f"🎓 Student: {self.name} | ID: {self.student_id}")
        print("📚 Enrolled Courses:")
        for course in self.courses:
            print(f"  - {course.name} (Credits: {course.credits}, Grade: {course.grade})")
        print(f"📊 Cumulative GPA: {self.calculate_gpa()}")
        print("-" * 40)

class StudentManagementSystem:
    """A class to manage the entire system and all students."""
    def __init__(self):
        self.students = {} # Dictionary to store students using their ID as the key

    def add_student(self, student_id, name):
        """Add a new student to the system."""
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"✅ Student '{name}' added to the system successfully.")
        else:
            print(f"⚠️ Student with ID {student_id} already exists!")

    def get_student(self, student_id):
        """Search for and retrieve a specific student by ID."""
        return self.students.get(student_id, None)

# ==========================================
# 🚀 Main Execution (Testing the code)
# ==========================================
if __name__ == "__main__":
    # 1. Initialize the system
    system = StudentManagementSystem()

    # 2. Add students
    system.add_student(202401, "Ahmed")
    system.add_student(202402, "Omar")

    # 3. Retrieve a student and enroll them in courses
    student1 = system.get_student(202401)
    if student1:
        student1.enroll_course("Data Structures", 3, "A")
        student1.enroll_course("Database Systems", 3, "B")
        student1.enroll_course("Calculus", 4, "A")

    # 4. Retrieve another student and enroll them in courses
    student2 = system.get_student(202402)
    if student2:
        student2.enroll_course("OOP", 3, "C")
        student2.enroll_course("Web Development", 3, "B")

    # 5. Display student reports
    student1.display_info()
    student2.display_info()