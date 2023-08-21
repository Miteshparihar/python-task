#Write a Python program to calculate surface volume and area of a cylinder 
# surface :- SA = 2πr**2 + 2πrh   
# volume :- V = πr**2h
# area :-  2 π r h
print('''
                    cylinder
        1. surface
        2. volume
        3. area
''')
user=int(input("Enter any choice to find :-"))
if user==1:
    radius=int(input("Enter radius :-"))
    hieght=int(input("Enter hieght :- "))
    surface=2*3.14*radius**2+2*3.14*radius*hieght
    print("surface of cylinder is :- ",surface)
elif user==2:
    radius=int(input("Enter radius :-"))
    hieght=int(input("Enter hieght :- "))
    volume=3.14*radius**2*hieght
    print("volume of cylinder is :- ",volume)
elif user==3:
    radius=int(input("Enter radius :-"))
    hieght=int(input("Enter hieght :- "))
    area=2*3.14*radius*hieght
    print(" Area of cylinder is :- ",area)
