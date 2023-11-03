'''
Explain Inheritance in Python with an example? What is init? Or What
Is A Constructor In Python?

Inheritance is a fundamental concept in object-oriented programming that allows
you to create a new class that inherits attributes and methods from an existing class.
The new class is often referred to as a "subclass" or "child class," and the existing class
is called the "superclass" or "parent class." Inheritance allows you to reuse and extend the
functionality of an existing class,promoting code reusability and maintaining a hierarchical
relationship between classes.

the __init__ method is a special method known as a constructor. It's used to initialize the
attributes or properties of an object when an instance of a class is created.
The constructor is automatically called when you create an object of that class.

'''
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())  
