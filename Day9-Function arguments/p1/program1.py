'''
Create a function which takes 2 arguments and returns sum,differnce,
 multiply,division,remindor,power
'''
def calculator(num1,num2):
    print(f'Caculator functions given inputs {num1,num2}')
    return num1 + num2, num1 - num2, num1 * num2, num1 / num2, num1 % num2, num1 * num2

num1 = int(input("Enter the 1st value: "))
num2 = int(input("Enter the 2nd value:" ))

print(f"Results of two arguments is: ",calculator(num1,num2))
print(f"Results of two arguments is: ",calculator(5,2))
print(f"Results of two arguments is: ",calculator(num1=5,num2=2))
print(f"Results of two arguments is: ",calculator(num2=2,num1=5))
print(f"Results of two arguments is: ",calculator(5)) # TypeError: calculator() missing 1 required positional argument: 'num2'