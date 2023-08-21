#How can you pick a random item from a list or tuple?
import random
inputTuple = (30,10, "TutorialsPoint", 20, "python", "code")
print("The given input tuple: ", inputTuple)
randomItem = random.choice(inputTuple)
print("The generated random tuple item = ", randomItem)
