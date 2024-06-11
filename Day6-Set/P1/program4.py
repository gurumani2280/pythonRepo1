a={99,324,7,0,755,88}
print(a)#{0, 99, 324, 755, 7, 88}

#a.pop(6)#TypeError: set.pop() takes no arguments (1 given)

x=a.pop()
print(a)#{99, 324, 755, 7, 88} Randomly remove the item
print(x)#0 whatever it's removed displayed here

#a.remove()#TypeError: set.remove() takes exactly one argument (0 given)
a.remove(99)
print(a)#{324, 755, 7, 88}

#a.remove(99)#KeyError: 99

#a.discard()#TypeError: set.discard() takes exactly one argument (0 given)
a.discard(324)
print(a)#{755, 7, 88}
a.discard(324)
print(a)#{755, 7, 88}

a.clear()
print(a)#set()
#a.pop()#KeyError: 'pop from an empty set'

