#Write a Python function to check whether a number is perfect or not. 
def perfect_number(number):
    if number <= 0:
        return False

    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i

    return divisors_sum == number

num = int(input("Enter a number: "))
if perfect_number(num):
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")

