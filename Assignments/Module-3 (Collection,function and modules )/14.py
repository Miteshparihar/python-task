#Write a Python program to find the second smallest number in a list.
list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
length = len(list1)
list1.sort()
print("Largest element is:", list1[length-1])
print("Smallest element is:", list1[0])
print("Second Largest element is:", list1[length-2])
print("Second Smallest element is:", list1[1])
 
