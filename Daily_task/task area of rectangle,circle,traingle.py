#task find area from user input.
#area of rectangle (length x width)
print("Find the area of reactangle")
length = int(input("length of rectangle:-"))
width = int(input("Width of rectangle:-"))
Area = length*width
print("Area of rectangle is :-",Area)

#area of circle (π x radius x radius)
print("Find area of a circle:-")
radius = int(input("radius of a circle:-"))
#area = π*radius*radius   ----this is not defined
area = 3.14*radius*radius # 22/7
print("Area of circle is :-",area)

#area of triangle (1/2 x Base x Height)
print("Find area of a triangle")
base = int(input("Base of tringle:- "))
height = int (input("Height of triangle:-"))
A = 1/2*base*height
print("Area of triangle:-",A) 
