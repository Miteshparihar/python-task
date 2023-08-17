#Game task 
import random
ln= random.randint(1,10)
print("Introduction to this game:- In this game there will be a lucky no. which will be between 1 to 15 and you will get 5 chances if lucky no. same in any 1 chance then you have won the game.")
status=True
count=0
while status:
        count+=1
        print("Chance",count)
        user=int(input("Enter any number:-"))
        if user>ln:
            print("Think lesser !")
        elif user<ln:
            print("Think bigger !")
        elif user==ln:
            print("You won the game !!")
            break
        else:
            print("You loss the game !!")
        if count>5:
            status=False
        else:
            status=True


    
    

    
    

    
    
