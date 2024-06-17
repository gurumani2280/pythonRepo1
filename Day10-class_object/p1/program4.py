class Dog:
    legs=4
    def __init__(self):
        print("This is constructor ")
        self.color="White"
myobj=Dog()
print(myobj.color)
myobj2=Dog()
myobj2.color="Brown"
print(myobj2.color)