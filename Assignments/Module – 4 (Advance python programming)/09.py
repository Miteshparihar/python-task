#09 Write a Python program to count the number of lines in a text file. 
def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return len(lines)
 
filename = 'basic.txt'  
print(f'The file {filename} has {count_lines(filename)} lines.')
