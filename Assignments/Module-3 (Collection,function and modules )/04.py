'''Write a Python function to get the largest number, smallest num and sum
of all from a list. '''
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst))
print("Minimum element in the list is :", min(lst))
print(" sum element in the list is :", sum(lst))
