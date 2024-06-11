a={4,89,'Test',4,89,876,'234&&&'}
print(a)#{89, '234&&&', 4, 'Test', 876}
print(type(a))#<class 'set'>
#print(a[3])#TypeError: 'set' object is not subscriptable
'''
Properties of Set
1-Duplicates are not allowed
2-Insertion order NOT maintained
3-Index is NOT available-indexing and slicing will not work
4-Hetrogeneous elements are allowed
5-Mutable or changeable
'''
b={}
print(type(b))#<class 'dict'>

c=set()
print(c)#set()
print(type(c))#<class 'set'>