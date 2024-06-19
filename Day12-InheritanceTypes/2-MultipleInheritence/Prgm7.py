#Multi level Inheritence :

class A :                                    # parent class of C
    def feature1(self):
        print("Feature 1 of Class A")
class B :                                  #Parent class of C
    def feature1(self):
        print("Feature 1 of Class B")
class C(A,B):                                  #Child class of A and B both, since class B is inhertited first
    def feature1(self):
        print("Feature 1 of Class C")
        B.feature1(self)
 #       super().feature1()

ObjC = C()

ObjC.feature1()      # this will print the class C print statement since its given first - Feature 1 of Class C because it is overridden

