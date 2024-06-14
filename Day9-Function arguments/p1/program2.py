'''
Create a function which takes 2 arguments and second arguments should be defalut to some value
and returns sum,differnce, multiply,division,remindor,power
'''
def calculator(num1,num2 = 1):
    print(f'Caculator functions given inputs {num1,num2}')
    return num1 + num2, num1 - num2, num1*num2, num1 / num2, num1 % num2, num1 * num2

print(f"Results of two arguments is: ",calculator(5))
print(f"Results of two arguments is: ",calculator(5,2))
print(f"Results of two arguments is: ",calculator(num1=5,num2=2))
print(f"Results of two arguments is: ",calculator(num2=2,num1=5))