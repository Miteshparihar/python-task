'''
What relationship is appropriate for Course and Faculty?

'''
class Faculty:
    def __init__(self, name, department):
        self.name = name
        self.department = department

class Course:
    def __init__(self, course_code, course_name, faculty):
        self.course_code = course_code
        self.course_name = course_name
        self.faculty = faculty
faculty1 = Faculty("Dr. Mitesh", "Computer Science")
faculty2 = Faculty("Prof. Raja", "Mathematics")

course1 = Course("BCA", "Introduction to Programming", faculty1)
course2 = Course("Btech", "Maths", faculty2)

