#Diffetent ways of creating sets using SET function
a=set("Hello")
print(a)#{'e', 'o', 'l', 'H'}

b=set(range(1,15,1))
print(b)#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

c=set([1,35,8,9,9])
print(c)#{8, 1, 35, 9}

d=set((56,89,89,66,7))
print(d)#{56, 89, 66, 7}

e=d.copy()
print(e)