a = {'a': 'Apple','b':"Banana",'m':'Mango',1:'one', 2:56, 3:'456'}

#deleting existing key

del a[1]
print(a)#{'a': 'Apple', 'b': 'Banana', 'm': 'Mango', 2: 56, 3: '456'}

# del a[1]#KeyError: 1 because 1 is already deleted

#another way of deleting key pair
#a.pop() #TypeError: pop expected at least 1 argument, got 0

a.pop('a')
print(a) #{'b': 'Banana', 'm': 'Mango', 2: 56, 3: '456'}

#a.pop('a') #KeyError: 'a'

a.popitem()
print(a)#{'b': 'Banana', 'm': 'Mango', 2: 56} randomly removes item

print(a.popitem())#(2, 56)
print(a)#{'b': 'Banana', 'm': 'Mango'}

a.clear()
print(a)#{}
#a.popitem() #KeyError: 'popitem(): dictionary is empty'
