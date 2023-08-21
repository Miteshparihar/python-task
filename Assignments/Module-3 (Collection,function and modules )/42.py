#Write a Python program to print all unique values in a dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2,'e':2,'f':4} 
unique_value = set() 
for value in my_dict.values():
  unique_value.add(value)
print(unique_value)
