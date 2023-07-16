#Write a Python program to get the Fibonacci series of given range
userinp=int(input("Enter a number:-"))
n1=0
n2=1
nextnum=0
count=1
while count<=userinp:
    print(nextnum,end=" ")
    count+=1
    n1=n2
    n2=nextnum
    nextnum=n1+n2
    total_no=n1+n2
