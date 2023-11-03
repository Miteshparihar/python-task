'''How Do You Handle Exceptions With Try/Except/Finally In Python?
Explain with coding snippets.'''
try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

