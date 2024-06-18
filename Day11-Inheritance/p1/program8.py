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
  def __init__(self,fname,lname,graduationyear):
    print("argument constructor of child class student",fname,lname,graduationyear)
    super().__init__(fname,lname)
    self.graduationyear=graduationyear

  def getgraduationyear(self):
    print(self.graduationyear)
  def isStudent(self):
    print("yes,a student")


x = Student("Mike", "Olsen",2004)
x.printname()
x.isStudent()
x.getgraduationyear()
'''
argument constructor of child class student Mike Olsen 2004
Aruguments constructor of parent person class
Mike Olsen
yes,a student
2004
'''