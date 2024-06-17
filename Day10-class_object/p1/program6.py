class Person:
    country="India"#static variable or class variable
    def __init__(self, name):
        self.name=name

print(Person.country)#India
Person.country="Bharat"
print(Person.country)#Bharat
myobj=Person("John")#object creation
print(myobj.country)#Bharat
print(myobj.name)
myobj2=Person("Peter")#another object created
print(myobj2.name)#AttributeError: 'Person' object has no attribute 'name'
print(myobj2.country)#Bharat
myobj2.name="max"
print(myobj2.name)