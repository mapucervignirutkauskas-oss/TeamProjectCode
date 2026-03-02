from project import Course, Student, University
import unittest
class Testproject(unittest.TestCase):
    #course class
    def test_course_init(self):
        c1 = Course("CSE1010", 3)
        self.assertEqual(c1.course_code, "CSE1010")
        self.assertEqual(c1.credits, 3)
        self.assertEqual(c1.students, [])

    def test_course_add_student_(self):
        c2 = Course("MATH2010", 3)
        s1 = Student("STU00001", "Student_1")
        c2.add_student(s1)
        self.assertEqual(c2.students, [s1])

    def test_duplicates(self):
        c3 = Course("PHYS1010", 2)
        s2 = Student("STU00002", "Student_2")
        c3.add_student(s2)
        c3.add_student(s2)
        self.assertEqual(c3.students, [s2])

    def test_get_student_count(self):
        c4 = Course("ECON1010", 2)
        s3 = Student("STU00003", "Student_3")
        s4 = Student("STU00004", "Student_4")
        s5 = Student("STU00005", "Student_5")
        c4.add_student(s3)
        c4.add_student(s4)
        c4.add_student(s5)
        self.assertEqual(c4.get_student_count(),3)

    #student class
    def test_init_student(self):
        s6 = Student("STU00006", "Student_6")
        self.assertEqual(s6.student_id, "STU00006")
        self.assertEqual(s6.name, "Student_6")
        self.assertEqual(s6.courses, {})

    def test_enroll(self):
        s7 = Student("STU00007", "Student_7")
        c5 = Course("CHEM1010", 3)
        s7.enroll(c5, 'A')
        self.assertEqual(c5.students, [s7])
    
    def test_calculate_gpa(self):
        s8 = Student("STU00008", "Student_8")
        c6 = Course("MATH1010", 3)
        c7 = Course("BIO1010", 3)
        c8 = Course("PSYCH1010", 2)
        s8.enroll(c6, 'A')
        s8.enroll(c7, 'B')
        s8.enroll(c8, 'C')
        val = round((3*4+3*3+2*2)/(3+3+2), 2) #3.12
        self.assertEqual(s8.calculate_gpa(), val)
    
    def test_get_courses(self):
        s9 = Student("STU00009", "Student_9")
        c9 = Course("PHYS2010", 2)
        c10 = Course("CSE3010", 2)
        c11 = Course("ENG1010", 3)
        s9.enroll(c9, 'B+')
        s9.enroll(c10, 'B-')
        s9.enroll(c11, 'C+')
        self.assertEqual(s9.get_courses(), [c9, c10, c11])

    #university class
    def test_init_university(self):
        u1 = University({"STU00010": Student("STU00010", "Student_10")},{"CSE1010": Course("CSE1010", 3)})
        self.assertEqual(list(u1.students.keys()), ["STU00010"])
        self.assertEqual(u1.students["STU00010"].name, "Student_10")
        self.assertEqual(list(u1.courses.keys()), ["CSE1010"])
        self.assertEqual(u1.courses["CSE1010"].credits, 3)
    
    def test_add_course(self):
        u2 = University()
        u2.add_course("CSE3100", 2)
        self.assertEqual(list(u2.courses.keys()), ["CSE3100"])
        self.assertEqual(u2.courses["CSE3100"].credits, 2)

    def test_duplicate_courses(self):
        u3 = University()
        u3.add_course("CSE2050", 2)
        u3.add_course("CSE2050", 2)
        self.assertEqual(list(u3.courses.keys()), ["CSE2050"])
        self.assertEqual(u3.courses["CSE2050"].credits, 2)
        self.assertEqual(len(u3.courses), 1)
    
    def test_add_student(self):
        u4 = University()
        u4.add_student("STU00011", "Student_11")
        self.assertEqual(list(u4.students.keys()), ["STU00011"])
        self.assertEqual(u4.students["STU00011"].name, "Student_11")

    def test_duplicate_students(self):
        u5 = University()
        u5.add_student("STU00012", "Student_12")
        u5.add_student("STU00012", "Student_12")
        self.assertEqual(list(u5.students.keys()), ["STU00012"])
        self.assertEqual(u5.students["STU00012"].name, "Student_12")
        self.assertEqual(len(u5.students), 1)

    def test_get_student_info(self):
        u6 = University()
        u6.add_student("STU00013", "Student_13")
        self.assertEqual(u6.get_student("STU00013"), u6.students["STU00013"])
        self.assertEqual(u6.get_student("STU00013").student_id, "STU00013")
        self.assertEqual(u6.get_student("STU00013").name, "Student_13")
        self.assertEqual(u6.get_student("STU00013").courses, {})

    def test_get_nonexistent_student_info(self):
        u7 = University()
        self.assertEqual(u7.get_student("STU00014"), None)

    def test_get_course(self):
        u8 = University()
        u8.add_course("ENG1010", 2)
        self.assertEqual(u8.get_course("ENG1010"), u8.courses["ENG1010"])
        self.assertEqual(u8.get_course("ENG1010").course_code, "ENG1010")
        self.assertEqual(u8.get_course("ENG1010").credits, 2)
        self.assertEqual(u8.get_course("ENG1010").students, [])
    
    def test_get_nonexistent_course(self):
        u9 = University()
        self.assertEqual(u9.get_student("STU00015"), None)
    
unittest.main()