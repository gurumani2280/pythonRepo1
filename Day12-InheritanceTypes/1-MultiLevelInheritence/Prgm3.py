class Shape :
    def calcarea(self):
        print("To calculate area create an obj of defined shape like square/rectangle etc")

class Rectangle(Shape):
    def __init__(self,length,width):
        print("init method of Rectangle",length,width)
        self.length = length
        self.width = width
    def calcarea(self):
        print("ares of rectangle is ",self.length*self.width)

class Square(Rectangle):
    def __init__(self,side):
        print("init method of square",side)
        super().__init__(side,side)

       # self.side = side
    def calcarea(self):
        print("area of square is ",self.length**2)

ObjSquare = Square(2)
#ObjRect = Rectangle(4,5)
#ObjSquare.calcarea()                  #area of square is  4
#ObjRect.calcarea()                    #ares of rectangle is  20
