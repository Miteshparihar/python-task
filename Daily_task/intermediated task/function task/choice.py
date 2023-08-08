def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

menu='''
            =========MENU==========

            1. Add
            2. Sub
            3. Quit
'''
print(menu)
choice=input("Enter your choice from menu : ")
x=int(input("Enter num 1: "))
y=int(input("Enrer num 2: "))

if choice=='1':
    
    print("Addition is : ",add(x,y))

elif choice=="n":
    pass
else:
    pass
