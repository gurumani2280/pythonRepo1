#take one user input and check if number is between 1 to 100
a=int(input('Please enter a number\n'))
if a>1 and a<100:
    print(f'{a} is between 1 to 100')
else:
    print(f'{a} is NOT between 1 to 100')