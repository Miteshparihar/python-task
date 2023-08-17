#Multiple level inheritance:
class P1:
    def hello(self):
        print("Hello good morning")
class P2:
    def hii(self):
        print("Hii good morning")
class C(P1,P2):
    def hey(self):
        print("Hey good morning")
obj1=C()
obj1.hey()
obj1.hello()
obj1.hii()
