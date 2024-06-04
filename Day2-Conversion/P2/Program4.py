#Float conversion
a=True
print(float(a)) #Output - 1.0
b=False
print(float(b)) #0.0
c=5
print(float(c))
d="abc"
#print(float(d)) #ValueError: could not convert string to float: 'abc'
e="1"
print(float(e)) #1.0
"""
for Boolean float conversion will work 
True - 1.0
False-0.0
for Int to float 
for 5 it is 5.0
for string if content is number it will work else throws error 
"ValueError: could not convert string to float: 'abc'"
"""
f="-10"
print(float(f))