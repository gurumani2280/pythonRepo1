class Person:
  def __init__(self, fname, lname):
    print("Aruguments constructor of parent person class")
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

  def isStudent(self):
    print("Not a student")

class Student(Person):
  def __init__(self,fname,lname):
    print("argument constructor of child class student",fname,lname)
    super().__init__(fname,lname)

  def isStudent(self):
    print("yes,a student")


x = Student("Mike", "Olsen")
x.printname()
x.isStudent()
