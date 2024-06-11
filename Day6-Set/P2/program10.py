a=set({10,20,30,40,50})
b=set({40,50,60,70,80})
print(a.symmetric_difference(b))#{80, 20, 70, 10, 60, 30}
print(a ^ b)#{80, 20, 70, 10, 60, 30}
print(a)#{50, 20, 40, 10, 30}
print(b)#{80, 50, 70, 40, 60}
print(b.symmetric_difference(a))#{80, 20, 70, 10, 60, 30}
print(b ^ a)#{80, 20, 70, 10, 60, 30}