m1= int(input("Enter a number:- "))
m2=int(input("Enter a number:- "))
m3=int(input("Enter a number:- "))
if m1>m2 and m1>m3:
    print("This is largest number:-",m1)
elif m2>m1 and m2>m3:
    print("This is largest number:-",m2)
elif m3>m1 and m2>m1:
    print("This is largest number:-",m3)
else:
    print("All are equal:-",m1,m2,m3)
  
