class Person:
    country="India"#static variable or class variable

print(Person.country)#India
Person.country="Bharat"
print(Person.country)#Bharat
myobj=Person()#object creation
print(myobj.country)#Bharat
myobj.name="John"#name is a instance attribute for myobj object only
print(myobj.name)
myobj2=Person()#another object created
#print(myobj2.name)#AttributeError: 'Person' object has no attribute 'name'
print(myobj2.country)#Bharat
myobj2.name="Peter"
print(myobj2.name)