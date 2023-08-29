#Core python Assesment test
status=True
while status:
    print('''---------------------Welcome to python E-Note---------------------
                  
                  Press 1 for generate Note
                  press 2 for view Note
                  press 3 for exit
             ''')
    user=int(input("Enter your choice:- "))
    if user==1:
        username=input("Enter python E-Note Generator Name :")
        if username.isdigit():
            print("Error")
        else:
            usertitle=input("Enter python E-Note Title : ")
            usercontent=input("Enter E-Note Content :")
            a=open("new.txt","w+")
            a.write(f"generater name:- {username}")
            a.write(f"\nE-note Title :- {usertitle}")
            a.write(f"\nE-note description:- {usercontent}")
            a.close()
    elif user==2:
         display=input("Do you want to display your Note ['y'/'n']:")
         if display=="y" or display=="yes":
             re=open("new.txt","r")
             print(re.read())
             re.close()
             status= False
         else :
             status=False
    elif user==3:
        print("You Exit !")
        status=False
             
     
         
