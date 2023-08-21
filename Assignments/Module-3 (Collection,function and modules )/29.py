# Write a Python program to unzip a list of tuples into individual lists.
l = [(1,2), (3,4), (8,4)] # list of tuples 
print(list(zip(*l))) # Zip and individual lists

