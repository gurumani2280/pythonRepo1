def person_details(*a,**b):
    print(a,type(a))
    print(b,type(b))
person_details()
'''
() <class 'tuple'>
{} <class 'dict'>
'''
person_details(name="Apple")
'''
() <class 'tuple'>
{'name': 'Apple'} <class 'dict'>
'''
person_details("Apple")
'''
('Apple',) <class 'tuple'>
{} <class 'dict'>
'''
