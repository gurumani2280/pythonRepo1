a="apple"
b="Test1"
print(a+b)
#print(a-b)#TypeError: unsupported operand type(s) for -: 'str' and 'str'
#print(a*b)#TypeError: can't multiply sequence by non-int of type 'str'
#print(a+1)#TypeError: can only concatenate str (not "int") to str
print(a+str(1))#apple1
print(a*2)#appleapple
print(a+str(1.1))
