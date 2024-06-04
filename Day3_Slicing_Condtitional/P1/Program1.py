a="Hello world I'm Apple"
print(f'value in a -  {a}')
print(f'Length of a - {len(a)}')
print(f'char at index 3 - {a[3]}')
print(f'char at index 20 - {a[20]}')
print(f'char at index -5 - {a[-5]}')
#print(f'char at index 25 - {a[25]}')#IndexError: string index out of range
#print(f'char at index -22 - {a[-22]}')#IndexError: string index out of range

print('a' in a)
print('h' in a)
print('H' in a)
print(' ' in a)
print('App' in a)
print('a' not in a)