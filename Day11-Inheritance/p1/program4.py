class Person:
  def __init__(self, fname, lname):
    print("Aruguments constructor of parent person class")
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self,fname,lname):
    print("argument constructor of child class student",fname,lname)


x = Student("Mike", "Olsen")#argument constructor of child class student Mike Olsen
x.printname()#AttributeError: 'Student' object has no attribute 'firstname'
