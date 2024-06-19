#Multi level Inheritence :

class A :                                    #Grandparent class of C / parent class of B
    def feature1(self):
        print("Feature 1 of Class A")
class B(A) :                                  #Child class of A / Parent class of C
    def feature2(self):
        print("Feature 2 of Class B")
class C(B):                                  #Child class of B / Grandchild class of A
    def feature3(self):
        print("Feature 3 of Class C")
ObjC = C()
ObjC.feature3()
ObjC.feature1()
ObjC.feature2()
