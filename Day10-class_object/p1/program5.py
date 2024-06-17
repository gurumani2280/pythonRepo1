class Dog:
    legs=4
    def __init__(self, color):
        print("This is constructor ")
        self.color=color
myobj=Dog("White")
print(myobj.color)
myobj2=Dog("Brown")
print(myobj2.color)