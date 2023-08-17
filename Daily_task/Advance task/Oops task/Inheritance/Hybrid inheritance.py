#Hybrid Inheritance
class A:
    def fun1(self):
        print("Hello func1")
class B(A):
    def fun2(self):
        print("Hello func2")
class D(A):
    def fun3(self):
        print("Hello fun3")
class C(D,B):
    def fun4(self):
        print("Hello fun4 ")
obj1=C()
obj1.fun1()
obj1.fun2()
obj1.fun3()
obj1.fun4()
