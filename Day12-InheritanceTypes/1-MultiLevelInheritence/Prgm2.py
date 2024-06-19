#Multi level Inheritence :

class A :                                    #Grandparent class of C / parent class of B
    def __init__(self,name,rollno):
        print("init method of Class A")
        self.name = name
        self.rollno = rollno

class B(A) :                                  #Child class of A / Parent class of C
    def __init__(self,name,rollno,age):
        print("init method of Class B")
        super().__init__(name,rollno)
        self.age =age
class C(B):                                  #Child class of B / Grandchild class of A
    def __init__(self,name,rollno,age,city):
        print("init method of Class C")
        super().__init__(name,rollno,age)
        self.city = city
    def PrintData(self):
        print("name",self.name)
        print("roll no",self.rollno)
        print("age",self.age)
        print("city",self.city)
ObjC = C("Tejaswini","44","30","Mysore")
ObjC.PrintData()


'''init method of Class C
init method of Class B
init method of Class A
name Tejaswini
roll no 44
age 30
city Mysore'''