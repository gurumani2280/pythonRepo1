'''
Create a function which takes variable length arguments and it return the sum of  all argument
'''


def sum(*num, a):
    print(f'Caculator functions given inputs {num},{a}')
    print(type(num))
    sum = a
    for i in num:
        sum = sum + i
    return sum


#print(f"Results of two arguments is: ", sum(2,3))#TypeError: sum() missing 1 required keyword-only argument: 'a'
print(f"Results of two arguments is: ", sum(2,a=3))
