'''Write a Python script to sort (ascending and descending) a dictionary by
value. '''
my_dict = {'c': 3,
           'a': 1,
           'd': 4,
           'b': 2}
 
sorted_dict = sorted([(value, key)
for (key, value) in my_dict.items()])

print("Sorted dictionary is :")
print(sorted_dict)
