# Python example to show the working of multiple
# inheritance

class Base1(object):
	def __init__(self):
		self.str1 = "Geek1"
		print("Base1")


class Base2(object):
	def __init__(self):
		self.str2 = "Geek2"
		print("Base2")


class Derived(Base2, Base1):
	def __init__(self):

		# Calling constructors of Base1
		# and Base2 classes
		super().__init__()
		Base1.__init__(self)
		print("Derived")

	def printStrs(self):
		print(self.str1, self.str2)


ob = Derived()
ob.printStrs()

'''
Base2
Base1
Derived
Geek1 Geek2
'''
