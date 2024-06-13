# addition of two numbers
def add(a,b):
    print("inside add() inputs", a,b)
    return a+b
# add() # TypeError: add() missing 2 required positional arguments: 'a' and 'b'

add(a=4,b=10) #inside add() inputs 4 10
print(add(5,30))
y=add(10,30)
print("addition",y)
add(b=88,a=10)