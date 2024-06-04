#Int conversion
b=False
print(int(b))
"""
For bool value Int conversion will either give 0(False) or 1(True)
"""
c=2.3
print(int(c))
"""
For Float Int conversion will remove the decimal part and integer part or Non decimal 
part will be returned as part of int conversion
"""

d="abc"
# print(int(d)) #ValueError: invalid literal for int() with base 10: 'abc'
e='123'
print(int(e)) #output -123
f='1.2'
#print(int(f)) #ValueError: invalid literal for int() with base 10: '1.2'
"""
For string Int func will check the content with in a string
if the content is Int then Int function can able to convert to Int else throws error
"""
g=''
print(int(g))#ValueError: invalid literal for int() with base 10: ''
