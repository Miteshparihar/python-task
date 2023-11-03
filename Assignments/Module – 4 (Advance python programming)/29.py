'''
What relationship is appropriate for Student and Person?
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

person1 = Person("John Smith", 30)
student1 = Student("Alice Johnson", 20, "S12345")
