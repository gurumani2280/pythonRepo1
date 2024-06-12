#using for loop
a = {'a': 'Apple','b':"Banana",'m':'Mango',1:'one', 2:56, 3:'456'}

for I in a:#here I is all keys of the Dic
    print(I,a[I])#only keys printed

for I in a.keys():
    print(I,a.get(I))