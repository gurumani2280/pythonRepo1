#Multi level Inheritence :

class A :                                    # parent class of C
    def feature1(self):
        print("Feature 1 of Class A")
class B :                                  #Parent class of C
    def feature1(self):
        print("Feature 1 of Class B")
class C(A,B):                                  #Child class of A and B both, since class A is inhertited first
    def feature3(self):
        print("Feature 3 of Class C")
ObjC = C()
ObjC.feature3()
ObjC.feature1()      # this will print the class A print statement since its given first - Feature 1 of Class A

