#method overriding
#super() used 3
class A:
    def add(self,a,b):
        print("Addition = ",a+b)
class B(A):
    def add (self,a,b):
        super().add(a,b)
        print("Multiplication = ",a*b)
obj=B()
obj.add(2,4)

