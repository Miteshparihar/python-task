#Hierarchical Inheritance
class A:
    def fun1(self):
        print ("This is a root")
class B(A):
    def fun2(self):
        print("This is class 1")
class C(A):
    def fun3(self):
        print("This is class 2")
class D(B):
    def fun4(self):
        print("This is C21")
class E(B):
    def fun(self):
        print("This is C22")
class F(B):
    def fun5(self):
        print("How are you")
class G(C):
    def fun6(self):
        print("Good morning")
class H(C):
    def fun7(self):
        print("hello c1")
ob1=D()
ob2=E()
ob3=F()
ob4=G()
ob5=H()
ob1.fun4()
ob1.fun2()
ob1.fun1()
ob2.fun()
ob3.fun5()
ob4.fun3()
ob4.fun6()
ob5.fun7()
