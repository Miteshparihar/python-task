#Menu choice by function:-
def Pizza(a):
    return a
def Burger(b):
    return b
def pani_puri(c):
    return c
def Dosa(d):
    return d
sum1=0
status=True
while status:
    print(''' ===============Welcome to tops restaurent===============
                                sr no.         Item                   Price
                                1.               Pizza                   90/-
                                2.              Burger                  89/-
                                3.              Panipuri                100/-
                                4.              Dosa                     80/-
    ''')
    user1=int(input("Enter your choice in menu:-"))
    if user1 == 1:
        print("Your item is:-",Pizza("pizza"))
        user=int(input("Enter Quantity :-"))
        total= user*90
        sum1+=total
        print("Total price:-",total)
    elif user1 == 2:
        print("Your item is:-",Burger("Burger"))
        user=int(input("Enter Quantity :-"))
        total= user*89
        sum1+=total
        print("Total price:-",total)
    elif user1 == 3:
        print("Your item is:-",pani_puri("panipuri"))
        user=int(input("Enter Quantity :-"))
        total= user*100
        sum1+=total
        print("Total price:-",total)
    elif user1 == 4:
        print("Your item is:-",Dosa("Dosa"))
        user=int(input("Enter Quantity :-"))
        total= user*80
        sum1+=total
        print("Total price:-",total)

    user2=input("Do you want to anything else ? ['y/n']:")
    if user2=='y' or user2=="yes":
        status=True
    else:
        print("Thank you !!!!")
        print("Your total bill:-",sum1)
        status=False
        
         
   
    
         
   
   
