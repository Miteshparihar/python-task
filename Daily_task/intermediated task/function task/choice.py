def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def exitq(a):
    return a
menu='''
            =========MENU==========

            1. Add
            2. Sub
            3. Quit
'''
print(menu)
choice=input("Enter your choice from menu : ")
if choice=='1':
    x=int(input("Enter num 1: "))
    y=int(input("Enter num 2: "))
    print("Addition is : ",add(x,y))

elif choice=="2":
    x=int(input("Enter num 1: "))
    y=int(input("Enter num 2: "))
    print("subtraction is : ",sub(x,y))
    
elif choice=="3":
    print(exitq("exit..."))



