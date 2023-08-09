''' task-1 :- print     1
                            1 1
                            1 1 1
                            1 1 1 1  '''
for i in range(4):
    for j in range(i+1):
        print("1",end=" ")
    print()
print("-----------------------------------")
'''  print               1 
                           1 0
                           1 0 1
                           1 0 1 0
                           1 0 1 0 1   '''
n =6  
for i in range(1, n):
    for j in range(1, i + 1):
        if j%2==1:
            print("1", end=" ")
        else:
            print("0",end=" ")
    print()

print("-----------------------------------")


'''
   print                 1
                           2 3
                           4 5 6
                           7 8 9 10 
'''
current_num = 1
stop = 2
rows = 4

for i in range(rows):
    for column in range(1, stop):
        print(current_num, end=' ')
        current_num += 1
    print("")
    stop += 1
print("-----------------------------------")
'''
  print                   A
                            B C
                            D E F
                            G H I J
                            K L M N O
'''
ascii_number = 65
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        character = chr(ascii_number)
        print(character, end=' ')
        ascii_number += 1
    print(" ")

    
print("--------------------------------------------------------------")


'''task : 2
              take user input as number and print the output table :
 '''

user= int(input("enter a number:-"))
for i in range(1,11):
    print(user,"x",i,"=",user*i)

''' task:-2
            take user input as number and print tables upto the number'''
user=int(input("Enter number and upto the table:-"))
for i in range(1,user):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
        
        
    

        

