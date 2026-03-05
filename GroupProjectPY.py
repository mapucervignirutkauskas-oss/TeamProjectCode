import csv




class Course:
    """Mapu Cervigni Rutkauskas: Represents a university course and stores enrolled students."""
    
    def __init__(self, course_code: str, credits: int, students=None):
        self.course_code = course_code
        #unique identifier for the course (e.g., "CSE1010")
        self.credits = credits
        #number of credits earned for completing the course.
        self.students = students if students is not None else []
        #all students enrolled in the course
    def __repr__(self):
        """Will return the string if just the Course class is called"""
        return f"Course(course_code = {self.course_code}, credits = {self.credits}, students = {self.students})"
    
    def add_student(self, student):
        """Adds a student to the student list only if they're not in the class"""
        if student not in self.students:
            self.students.append(student)


    def get_student_count(self):
        return len(self.students)

class Student:
    """Mapu Cervigni Rutkauskas: Adds a student to the course roster if they are not already enrolled."""

    def __repr__(self):
        return f"Student({self.student_id!r}, {self.name!r})"

    GRADE_POINTS = { 'A' : 4.0, 'A-' : 3.7, 'B+': 3.3, 'B' : 3.0, 'B-' : 2.7, 'C+': 2.3, 'C' : 2.0, 'C-' : 1.7, 'D' : 1.0, 'F' : 0.0 }
    def __init__(self, student_id: str, name: str, courses=None):
        self.student_id = student_id
        #unique identifier for the student.
        self.name = name
        #the student’s name
        self.courses = courses if courses is not None else {}
    def enroll(self, course, grade):
        if grade not in self.GRADE_POINTS:
            raise ValueError(f"Invalid grade: {grade}")
        self.courses[course] = grade
        course.add_student(self)
    def update_grade(self, course, grade):
        if grade not in self.GRADE_POINTS:
            raise ValueError(f"Invalid Grade: {grade} is not accepted.")
        if course not in self.courses:
            raise ValueError("Student is not enrolled in this course")
        self.courses[course] = grade
    def calculate_gpa(self):
        total_points = 0
        total_credits = 0
        for course, grade in self.courses.items():
            if grade not in self.GRADE_POINTS:
                raise ValueError(f"Invalid Grade: {grade} is not accepted.")
            grade_points = self.GRADE_POINTS[grade]
            total_points += grade_points * course.credits
            total_credits += course.credits
        if total_credits == 0:
            return 0.0
        return round(total_points / total_credits, 2)
    def get_courses(self):    
        return list(self.courses.keys())
    def get_course_info(self):
        info = []

        for course, grade in self.courses.items():
            info.append({"course_code": course.course_code, "grade": grade, "credits": course.credits})

        return info
    
#c1 = Course("CSE1010", 3)
#c2 = Course("MATH2010", 4)

#s1 = Student("STU00001", "Bob")

#s1.enroll(c1, "A")
#s1.enroll(c2, "B+")

#print(s1.get_courses())

class University:
    def __init__(self, students=None, courses=None):
        self.students = students if students is not None else {}
        self.courses = courses if courses is not None else {}

    def add_course(self, course_code, credits):
        if course_code not in self.courses:
            self.courses[course_code] = Course(course_code, credits)
        return self.courses[course_code]
    
    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
        return self.students[student_id]
    
    def get_student(self, student_id):
        if student_id not in self.students:
            return None
        else:
            return self.students[student_id]
        
    def get_course(self, course_code):
        if course_code not in self.courses:
            return None
        else:
            return self.courses[course_code]
        
    def get_course_enrollment(self, course_code):
        return self.courses[course_code].get_student_count()
    
    def get_students_in_course(self, course_code):
        return self.courses[course_code].students
    
"""All csv - related: Done by Mapu Cervigni Rutkauskas"""
u_files = University()

with open('course_catalog.csv') as courses:
    csv_reader1 = csv.reader(courses)
    next(csv_reader1)
    for row in csv_reader1:
        course_code = row[0]
        credits = row[1]
        u_files.add_course(course_code, credits)


with open('university_data.csv') as uni_data:
    """Opens the data csv and names it uni_data"""
    csv_reader2 = csv.reader(uni_data)
    """Skips first line"""
    next(csv_reader2)
    for row in csv_reader2:
        student_id = row[0]
        name = row[1]
        course_entries = row[2].split(";")

        student = u_files.add_student(student_id, name)

        for entry in course_entries:
            if entry.strip() == "":
                continue
            parts = entry.split(":")
            course_code = parts[0]
            grade = parts[1]

            course = u_files.get_course(course_code)
            if course:
                student.enroll(course, grade)


print(u_files.students)
print(u_files.courses)


"""
u = University()

u.add_student("STU00001", "burh")
print(u.get_student("STU00001"))
u.add_course("CSE2050", 2)
print(u.get_course("CSE2050"))
u.get_student("STU00001").enroll(u.get_course("CSE2050"), 'A')
print(u.get_course_enrollment("CSE2050"))
print(u.get_students_in_course("CSE2050"))
print(u.get_student("STU00001").calculate_gpa())
u.add_course("MATH2010", 3)
u.get_student("STU00001").enroll(u.get_course("MATH2010"), 'B')
print(u.get_student("STU00001").calculate_gpa())
    
"""