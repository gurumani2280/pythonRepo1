#Take numerid user input and display respective alphabetical value
a=int(input('Please enter a number between 0 to 5\n'))
numbers = ['Zero','one','two','three','four','five']
if a<=5:
    print(numbers[a])
else:
    print("Enter valid value between 0 to 5")
