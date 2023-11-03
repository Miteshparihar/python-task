'''
Write a Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle 
'''

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159265358979323846 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159265358979323846 * self.radius
    
radius = 5.0  
my_circle = Circle(radius)

print("Radius:", my_circle.radius)
print("Area:", my_circle.area())
print("Perimeter:", my_circle.perimeter())
