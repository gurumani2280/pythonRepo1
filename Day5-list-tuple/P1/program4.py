x=[8,6,54]
x.remove(6)
print(x)#[8, 54]
#x.remove(10)#ValueError: list.remove(x): x not in list
#x.pop()#removes last element
print(x)#[8]
#x.append(55,77,88)#TypeError: list.append() takes exactly one argument (3 given)
#print(x)
x.append(55)
x.pop(2)
print(x)
x.clear()
print(x)

x=[5,9,77,89]
del x[3]
print(x)

x=[5,9,77,89,'test',999]
del x[3:5]
print(x)#[5, 9, 77, 999]