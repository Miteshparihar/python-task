#Write a Python program to check whether a list contains a sub list.
l1=[1,2,[3,4,5],6,7]
l2=[3,4,5]
if l2 in l1:
    print("This is sub list")
else:
    print("Not a sub list")
