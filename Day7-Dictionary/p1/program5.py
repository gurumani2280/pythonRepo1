#find the frequency of each character of given word
a=input(" enter valid string")
d={}
for I in a:
    value=d.get(I,0)
    d.update({I:value+1})
    #print(d)

print(d)
