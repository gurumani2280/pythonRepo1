a=set({10,20,30,40,50})
b=set({40,50,60,70,80})
print(a.difference(b))#{10, 20, 30}
print(a - b)#{10, 20, 30}
print(a)#{50, 20, 40, 10, 30}
print(b)#{80, 50, 70, 40, 60}
print(b.difference(a))#{80, 60, 70}
print(b - a)#{80, 60, 70}