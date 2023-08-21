#Write a Python program to create a dictionary from a string. 
def letter_count_dict(string):
    letter_count = {}
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

sample_string = 'Tops Technology'
result = letter_count_dict(sample_string)
print(result)
