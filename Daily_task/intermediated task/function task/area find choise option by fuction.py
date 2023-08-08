#function task-1 (find area with choise any one )
def circle(r):
    pi=3.14
    return pi*r**2
def triangle( bredth,heigth):
    return 1/2*bredth*heigth
def rectangle(length,bredth):
    return length*bredth

status=True
while status:
    print('''
             =============Area Finder============
             1. Area of circle?
             2. Area of triangle?
             3.Area of Rectangle?
    ''')
    user=int(input("Enter your choice (Write in number like 1,2,3...) :- "))
    if user==1:
        radius=float(input("Enter radius of circle:-"))
        print("Area of circle is:-",circle(radius))
    elif user==2:
        bredth=int(input("Enter bredth of triangle:-"))
        heigth=int(input("Enter height of triangle:-"))
        print("Area of traingle is:-",triangle(bredth,heigth))
    elif user==3:
        length=int(input("Enter length of rectangle:-"))
        bredth=int(input("Enter bredth of rectangle:-"))
        print("Area of traingle is:-",rectangle(bredth,length))

    choice=input("Do You want to continue ? ['y/n'] : ")
    if choice=='y' or choice=='yes':
        status=True
    else:
        status=False
