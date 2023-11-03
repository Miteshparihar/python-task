# 12. Write a Python program to copy the contents of a file to another file.
with open("items.txt") as f:
    with open("basic.txt", "w") as f1:
        for line in f:
            f1.write(line)
