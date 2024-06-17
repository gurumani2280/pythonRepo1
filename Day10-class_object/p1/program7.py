class Employee:
    companyname="Wipro"
    def __init__(self, name,salary):
        print("This is a constructor and It will get executed whenever the object of employee class is creted")
        self.name=name
        self.salary=salary
    def printEmployeeDetails(self):
        print(f"company name-{self.companyname},Employee name-{self.name},Salary-{self.salary}")

myobj=Employee("John",5000)
myobj.printEmployeeDetails()
