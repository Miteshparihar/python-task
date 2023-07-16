'''Write python program that swap two number with temp variable and
without temp variable.'''
# swapping of two variables
x = 10
y = 50
 
# Swapping of two variables
# Using third variable
temp = x
x = y
y = temp
 
print(" x=", x)
print("y=", y)

#Without third variable
x = 5
y = 7
 
print ("Before swapping: ")
print(" x : ", x)
print("y :",y)
# code to swap 'x' and 'y'
x=y
y=x-2
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
