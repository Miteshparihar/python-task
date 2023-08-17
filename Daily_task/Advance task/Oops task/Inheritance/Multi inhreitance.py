#multi inheritance
class Parentp:
    def hello(self):
        print("Hello good morning")
class a(Parentp):
    def hi(self):
        print("Hiii good morning")
class b(a):
    def hey(self):
        print("Hey good morning")
obj1=b()
obj1.hello()
obj1.hi()
obj1.hey()

