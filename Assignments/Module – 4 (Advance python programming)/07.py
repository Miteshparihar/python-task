#Write a Python program to read a file line by line store it into a variable.

read=open("basic.txt","r")
#stored in variable
a=read.readlines()
print(a)
read.close()
