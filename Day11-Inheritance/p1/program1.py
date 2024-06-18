class A:
    def __init__(self):
        print("No argument constructor")
    def __init__(self,var1):
        print("argument constructor",var1)
myobj1=A()#TypeError: A.__init__() missing 1 required positional argument: 'var1'
