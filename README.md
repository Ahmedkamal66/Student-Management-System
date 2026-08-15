# 🎓 Student Management System (OOP in Python)

A robust, cleanly structured Python application designed to manage student enrollments, track courses, and calculate Cumulative GPAs. 

This project was built to demonstrate core **Object-Oriented Programming (OOP)** concepts, clean code architecture, and efficient data structure utilization. It serves as an excellent educational example for undergraduate Computer Science students learning Python.

## 🌟 Features
- **Add New Students:** Register students with unique IDs and names.
- **Course Enrollment:** Enroll students in specific courses with credit hours and letter grades.
- **Automated GPA Calculation:** Dynamically calculates the Cumulative GPA based on standard university grading systems, handling edge cases (e.g., zero enrolled credits).
- **Academic Transcript Generation:** Displays a cleanly formatted report of a student's enrolled courses, grades, and current GPA.

## 📚 Educational Value & Concepts Covered
As an academic project, this codebase is specifically designed to teach and demonstrate:
1. **Encapsulation:** Segregating data into logical entities (`Course`, `Student`, `System`).
2. **Data Structures:** 
   - Using **Lists** for dynamic course enrollments.
   - Using **Dictionaries (Hash Maps)** for $O(1)$ fast retrieval of student records by ID.
3. **Error Handling & Edge Cases:** Preventing `ZeroDivisionError` during GPA calculations.
4. **Documentation:** Proper use of Python Docstrings and clean, readable variable naming conventions.

## 🛠️ Technologies & Tools
- **Language:** Python 3.x
- **Paradigm:** Object-Oriented Programming (OOP)
- **Version Control:** Git & GitHub

## 📂 Code Structure (Classes)
* `Course`: Represents an individual academic course (Name, Credits, Grade).
* `Student`: Represents a university student. Contains methods to enroll in courses and calculate GPA.
* `StudentManagementSystem`: The core engine that stores all students in a dictionary and handles retrieval and registration.
