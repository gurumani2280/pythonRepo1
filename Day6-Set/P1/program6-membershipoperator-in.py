a="hello"
print('a' in a)#False
print('l' in a)#True
print('l' not in a)#False

#b=list(11,88,99)#TypeError: list expected at most 1 argument, got 3

b=list([11,88,99])
print(b)
print(11 in b)#True
print('11' in b)#False

c=set(["hello",88,67,67,67])
print(c)#{'hello', 67, 88}
print(88 in c)#True