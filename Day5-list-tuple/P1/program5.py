x=()
print(x)
print(type(x))#<class 'tuple'>
y=(11)
print(y)
print(type(y))#<class 'int'>

y=(11,)#always with comma
print(y)
print(type(y))#<class 'tuple'>

y.append(33)#AttributeError: 'tuple' object has no attribute 'append'