def reverse(num):
    print(num)
    if num<=1:
        return 1
    else:
        return reverse(num-1)
reverse(500)
