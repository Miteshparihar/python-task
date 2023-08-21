#method overloading
#so this method is not run
#And use default value and run program
class Method:
    '''def add(self,a,b):
        print("Addition =",a+b)'''
    def add(self,a,b=0,c=0):
        print("Addition =",a+b+c)
obj=Method()
obj.add(15,20,34)
