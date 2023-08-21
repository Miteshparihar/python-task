#Write a Python function to calculate the factorial of a number (anonnegative integer) 
def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
num = 5
fact = factorial(num)
print(f"The factorial of {num} is {fact}")
