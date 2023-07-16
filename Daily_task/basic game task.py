#Game task 
import random
ln= random.randint(1,10)
print("Introduction to this game:- In this game there will be a lucky no. which will be between 1 to 15 and you will get 5 chances if lucky no. same in any 1 chance then you have won the game.")
while True:
    print("chance-1")
    user=int(input("Enter any number:-"))
    if user<1 or user>15:
        print("please enter number between 1 to 15")
        continue
    elif user==ln:
        print("Congrats! you won the game")
        print("Your lucky no. is :- ",ln)
        break
    print("chance-2")
    user=int(input("Enter any number:-"))
    if user<1 or user>15:
        print("please enter number between 1 to 15")
        continue
    elif user==ln:
        print("Congrats! you won the game")
        print("Your lucky no. is :- ",ln)
        break
    print("chance-3")
    user=int(input("Enter any number:-"))
    if user<1 or user>15:
        print("please enter number between 1 to 15")
        continue
    elif user==ln:
        print("Congrats! you won the game")
        print("Your lucky no. is :- ",ln)
        break
    print("chance-4")
    user=int(input("Enter any number:-"))
    if user<1 or user>15:
        print("please enter number between 1 to 15")
        continue
    elif user==ln:
        print("Congrats! you won the game")
        print("Your lucky no. is :- ",ln)
        break
    print("chance-5")
    user=int(input("Enter any number:-"))
    if user<1 or user>15:
        print("please enter number between 1 to 15")
        continue
    elif user==ln:
        print("Congrats! you won the game")
        print("Your lucky no. is :- ",ln)
        break
    else:
        print("you loss the game")
        print("Your lucky no. is :- ",ln)
    break

    
    

    
    

    
    
