def natural(x):
    if x<=1:
        return 1
    else:
        return x+natural(x-1)
user=int(input("Enter number:-"))
print("Natural number is upto :-",natural(user))

