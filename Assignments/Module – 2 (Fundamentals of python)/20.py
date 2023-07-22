'''Write a Python function that takes a list of words and returns the length
of the longest one. '''
def long(words):
    check=max(words,key=len)
    print("longest word =", check,
          ", length=", len(check))
 # Driver Program
a = ["one", "two", "third", "four"]
long(a)
