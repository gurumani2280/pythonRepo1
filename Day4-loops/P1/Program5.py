#To get the sum of 1 to user input
a=1
b=int(input("Please enter a number\n"))
sum=0
while a<=b:
    sum=sum+a
    a=a+1
else:
    print("Condition is false",a)

print("sum",sum)
print("sum using formula",(b*(b+1))//2)