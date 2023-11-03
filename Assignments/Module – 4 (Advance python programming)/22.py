'''
How to Define a Class in Python? What Is Self? Give An Example Of
A Python Class

Ans:-
         define a class using the class keyword. A class is a blueprint for creating
         objects (instances) that have attributes and methods. The self keyword is
         used as the first parameter of class methods to refer to the instance of the class.
         It is similar to this in some other programming languages.

         
'''
class ClassName:
    
    def __init__(self, parameter1, parameter2):
        self.instance_attribute1 = parameter1
        self.instance_attribute2 = parameter2
    
    def instance_method(self):
        print("Instance method called with attribute values:", self.instance_attribute1, self.instance_attribute2)
