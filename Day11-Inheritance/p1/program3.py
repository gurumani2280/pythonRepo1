class Person:
  def __init__(self, fname, lname):
    print("Aruguments constructor of parent person class")
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self):
    print("No argument constructor of child class student")

x = Student("Mike", "Olsen") #TypeError: Student.__init__() takes 1 positional argument but 3 were given
x.printname()
