class Employee:
    companyname="Wipro"
    weeklyworkinghours=45
    def __init__(self, name,salary):
        print("This is a constructor and It will get executed whenever the object of employee class is creted")
        self.name=name
        self.salary=salary
    def printEmployeeDetails(self):
        print(f"company name-{self.companyname},Employee name-{self.name},Salary-{self.salary}")

    @classmethod
    def displayWorkHours(cls):
        print(f"Company Name {cls.companyname} working hours {cls.weeklyworkinghours}")

    @staticmethod
    def maximumoftwonumbers(a1,a2):
        return max(a1,a2)

myobj=Employee("John",5000)
myobj.printEmployeeDetails()
myobj.displayWorkHours()
print(myobj.maximumoftwonumbers(45,88))