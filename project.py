import csv
class Course:
    
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
if __name__ == "__main__":
    #create the university object
    u = University()

    #open the course catalog file and add courses by row
    with open('course_catalog.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            u.add_course(row['course_code'], int(row['credits']))

    #open the university data file and add students by row
    with open('university_data.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            u.add_student(row['student_id'], row['name'])
            s_courses = row['courses'].split(sep=";")
            dictformat = {}
            for c in s_courses:
                course_id, grade = c.split(":")
                dictformat[course_id] = grade
            for course_id in dictformat:
                u.get_student(row['student_id']).enroll(u.get_course(course_id), dictformat[course_id])

    #demonstrations

    #list of students enrolled in course
    print(u.get_students_in_course('CSE2050'))

    #gpa of a student
    print(u.get_student("STU00100").calculate_gpa())

    #all courses and course_info for a student
    print(u.get_student("STU00050").get_courses())
    print(u.get_student("STU00050").get_course_info())

    #mean gpa all students
    temp = 0
    for student_id in u.students:
        temp += u.get_student(student_id).calculate_gpa()
    print(round(temp/len(u.students),2))

    #median gpa all
    gpas = []
    for student in u.students.values():
        gpa = student.calculate_gpa()
        gpas.append(gpa)
    gpas_sorted = sorted(gpas)
    if len(gpas) % 2 == 1:
        print(gpas_sorted[len(gpas)//2])
    else:
        print(round((gpas_sorted[len(gpas)//2-1]+gpas_sorted[len(gpas)//2])/2, 2))

    #the course
    course = u.get_course("BUS1010")
    
    #mean gpa for the course
    sum = 0
    for student in course.students:
        grade = student.courses[course]
        points = Student.GRADE_POINTS[grade]
        sum += points
    print(round(sum/u.get_course_enrollment(course.course_code), 2))
        
    #mode gpa for the course
    grade_count = {}
    for student in course.students:
        grade = student.courses[course]

        if grade in grade_count:
            grade_count[grade] += 1
        else:
            grade_count[grade] = 1
    count = 0
    modes = []
    for grade in grade_count:
        max = grade_count[grade]
        if max > count:
            count = max
            modes = [grade]
        elif max == count:
            modes.append(grade)
    print(modes)

    #median gpa for the course
    grades = []
    for student in course.students:
        grade = student.courses[course]
        points = Student.GRADE_POINTS[grade]
        grades.append(points)
    sorted_grades = sorted(grades)
    if len(grades) % 2 == 1:
        print(sorted_grades[len(grades)//2])
    else:
        print(round((sorted_grades[len(grades)//2-1] + sorted_grades[len(grades)])/2, 2))

    #other course for common students between courses
    other_course = u.get_course("CSE1010")

    #common students between courses
    common_students = []
    for student in course.students:
        if student in other_course.students:
            common_students.append(student)
    print(common_students)