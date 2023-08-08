#Write a Python program to check a list is empty or not.
lst = [1,2,1,2]     #using not operator
if not lst:
  print("List is empty")
else:
    print("list is not empty")
#using len()

lst = []

# Checking whether the list size is equal to 0
if len(lst) == 0:
   print('Empty list')
else:
   print('Not Empty list')
