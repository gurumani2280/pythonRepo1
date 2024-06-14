'''
Create a function which takes variable length arguments and it return the sum of  all argument
'''
def sum(*num):
    print(f'Caculator functions given inputs {num}')
    sum=0
    for i in num:
        sum=sum+i
    return sum
print(f"Results of two arguments is: ",sum())
print(f"Results of two arguments is: ",sum(5))
print(f"Results of two arguments is: ",sum(5,2))
print(f"Results of two arguments is: ",sum(5,3,2))
print(f"Results of two arguments is: ",sum(5,3,5,6))