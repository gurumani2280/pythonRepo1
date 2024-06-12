a = {'a': 'Apple','b':"Banana",'m':'Mango',1:'one', 2:56, 3:'456'}
#accessing dic.value based on key value
print(a['m']) #Mango
#print(a[23]) #KeyError: 23

#using get() function

print(a.get('m')) #Mango
print(a.get(23)) #None
print(a.get(23,'Key Not present'))

# adding new key value and modifying the existing key value
a[4]="Four"
print(a) # {'a': 'Apple', 'b': 'Banana', 'm': 'Mango', 1: 'one', 2: 56, 3: '456', 4: 'Four'}

a[3]='Three'
print(a) #{'a': 'Apple', 'b': 'Banana', 'm': 'Mango', 1: 'one', 2: 56, 3: 'Three', 4: 'Four'}
print(len(a)) #7

a.update({5:'Five'})
print(a)#{'a': 'Apple', 'b': 'Banana', 'm': 'Mango', 1: 'one', 2: 56, 3: 'Three', 4: 'Four', 5: 'Five'}

a.update({2:'Two'})
print(a)#{'a': 'Apple', 'b': 'Banana', 'm': 'Mango', 1: 'one', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}

# to get all keys inside Dic
print(a.keys())#dict_keys(['a', 'b', 'm', 1, 2, 3, 4])

#to get key values
print(a.values())#dict_values(['Apple', 'Banana', 'Mango', 'one', 56, 'Three', 'Four'])

print(a.items())#dict_items([('a', 'Apple'), ('b', 'Banana'), ('m', 'Mango'), (1, 'one'), (2, 56), (3, 'Three'), (4, 'Four')])

a.update({6:'six',7:'Seven'})#{'a': 'Apple', 'b': 'Banana', 'm': 'Mango', 1: 'one', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'six', 7: 'Seven'}
print(a)