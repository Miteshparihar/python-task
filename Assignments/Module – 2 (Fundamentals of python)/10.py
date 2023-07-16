'''Write a Python program that will return true if the two given integer
values are equal or their sum or difference is 5. '''
a = int(input("enter a ="))

b = int(input("enter b ="))

#defining a function

def result(a,b):
    if(a == b or (a-b) == 5 or(a+b) == 5):

       return True
    else:

       return False

#printing the result

print(result(a,b))
   
    
  
