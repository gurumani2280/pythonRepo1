#a=frozenset(99,22,33,44,66,00,44,22,33)#TypeError: frozenset expected at most 1 argument, got 9
a=frozenset([3,"hello",66,77,88,88,99])#
print(a)#frozenset({66, 3, 99, 77, 88, 'hello'})
print(type(a))#<class 'frozenset'>

a.pop()#AttributeError: 'frozenset' object has no attribute 'pop'
