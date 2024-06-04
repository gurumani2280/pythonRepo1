#while loop-To print all character of a given string along with index
a='hello world'
index=0
while index<len(a):
    print(a[index],index)
    index=index+1
else:
    print("\nfor loop ended,all character printed")
