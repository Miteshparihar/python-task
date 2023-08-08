#choice operation board
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def exit(a):
    return a
print('''
           operations choice board
           1. Addition
           2.Substraction
           3.Multiplication
           4.Division
           5.Modulo
           6.Exit
''')
user=int(input("Enter your choice (1,2,3...):-"))
if user==1:
    a=int(input("Enter a number_1:-"))
    b=int(input("Enter a number_2:-"))
    print("Addition is :-",add(a,b))
elif user==2:
    a=int(input("Enter a number_1:-"))
    b=int(input("Enter a number_2:-"))
    print("substraction is :-",sub(a,b))
elif user==3:
    a=int(input("Enter a number_1:-"))
    b=int(input("Enter a number_2:-"))
    print("Multiplication is :-",multi(a,b))
elif user==4:
    a=int(input("Enter a number_1:-"))
    b=int(input("Enter a number_2:-"))
    print("division is :-",div(a,b))
elif user==5:
    a=int(input("Enter a number_1:-"))
    b=int(input("Enter a number_2:-"))
    print("reminder is :-",mod(a,b))
elif user==6:
   print(exit("exit.."))
    
