#To print numbers from 1 to till user input number
a=1
b=int(input("Please Enter a number till you want to print\n"))
while a<=b:
   # print(a)
    print(a,end=" ")
    a=a+1

print("\noutside of while loop",a)