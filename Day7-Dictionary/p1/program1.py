'''
Dictionary is used for key value pair
it is mutable
Dictionary key can not be duplicate
If we try to add duplicate key then existing value will be overridden
'''

# Creating empty dic.
 # we have two ways to create empty dictionry
x = {}
print(x, type(x)) # {} <class 'dict'>

  #OR#

y = dict()
print(y, type(y)) # {} <class 'dict'>
print(len(y)) # 0

# create dic. with some key vale pair

a = {'a': 'Apple','b':"Banana",'m':'Mango',1:'one', 2:56, 3:'456'}
print(len(a)) # 6
print(a) # {'a': 'Apple', 'b': 'Banana', 'm': 'Mango', 1: 'one', 2: 56, 3: '456'}