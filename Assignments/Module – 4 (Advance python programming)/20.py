'''Write python program that user to enter only odd numbers, else will
raise an exception. '''
while True:
    try:
        number = int(input("Enter an odd number: "))
        if number % 2 == 0:
            raise ValueError("Even number entered. Please enter an odd number.")
        else:
            print("You entered an odd number:", number)
            break  
    except ValueError as e:
        print(e)
