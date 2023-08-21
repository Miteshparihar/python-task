#Write a Python function to check whether a number is in a given range
def range_bet(number, lower, upper):
    return lower <= number <= upper
num = 15
lower = 10
upper = 20
if range_bet(num, lower, upper):
    print(f"{num} is in the range between {lower} and {upper}.")
else:
    print(f"{num} is not in the range between {lower} and {upper}.")
