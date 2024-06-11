a={45,89,11,4,90,0,87,65,42,42,45}
print(a)#{0, 65, 4, 42, 11, 45, 87, 89, 90}
print(len(a))#9
a.add(999)
print(a)#{0, 65, 4, 999, 42, 11, 45, 87, 89, 90}
a.add(45)
print(a)#{0, 65, 4, 999, 42, 11, 45, 87, 89, 90}
#Add is to add single element to set

#a.update(1,5)#TypeError: 'int' object is not iterable

a.update([1,5])
print(a)#{0, 65, 1, 4, 5, 999, 42, 11, 45, 87, 89, 90}

a.update([1,5],(777,666),"Welcome")
print(a)#{0, 1, 4, 5, 777, 11, 666, 42, 45, 'o', 'W', 'l', 'e', 65, 'm', 87, 89, 90, 999, 'c'}