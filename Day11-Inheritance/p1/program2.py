class Person:
  def __init__(self, fname, lname):
    print("Aruguments constructor of parent person class")
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()
'''
Aruguments constructor of parent person class
Mike Olsen

'''