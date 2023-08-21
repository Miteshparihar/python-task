''' Write a Python program to combine two dictionary adding values for
common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). '''
def combine_dicts(dict1, dict2):
    dict3 = dict1.copy()
    for i, j in dict2.items():
        if i in dict3:
            dict3[i] += j
        else:
            dict3[i] = j

    return dict3
dict1 = {'a': 10, 'b': 200, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}
combined = combine_dicts(dict1, dict2)
print(combined)



