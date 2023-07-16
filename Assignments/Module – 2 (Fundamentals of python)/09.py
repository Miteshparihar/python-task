'''Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero. '''
x=int(input("Enter a number 1:-"))
y=int(input("Enter a number 2:-"))
z=int(input("Enter a number 3:-"))
total_sum=0
if x==y or y==z or z==x:
    print(total_sum)
else:
    total_sum=x+y+z
    print(total_sum)
    
