# ##### 1. Topic unpacking ########################
m = [10, 20, 30]
# here list is unpacked into x, y, z
x,y,z = m  # x is 10, y is 20, z is 30
print(f'{x=}, {y=}, {z=}') 

# Can we unpack a dict?
d = {'a':1, 'b':2, 'c':3}
x,y,z = d

# Unpacking involves iteration. So when you say
# x,y,z = m
# Python iterates over m. Each element it gets back during that iteration is assigned to one of the variables.
# So unpacking a list or tuple gives you its elements. Unpacking a string is weird, but gives you its characters.
# unpacking above dictionary , get all the keys of dictionary
# x,y,z = d  # x is 'a', y is 'b', and z is 'c'
# If we really and truly want to unpack a dict with its values, can we? Yes! Just use the items method:
# x,y,z = d.items() 
# Since dict.items returns (key, value) tuples, you'll then get that:
# - x is ('a', 1)
# - y is ('b', 2)
# - z is ('c', 3)

# Did you know you can do *nested* unpacking?

m = [10, 20, [70, 80, 90]]
x,y,(a,b,c) = m
print(f'{x=}, {y=}, {a=}, {b=}, {c=}')

# #### 2. Topic split ########################
s = 'ab cd:ef gh'
s.split(' ')  # ['ab', 'cd:ef', 'gh']
s.split(':')  # ['ab cd', 'ef gh']

# Q: Can we split on either ' ' or ':'?
# A: Not with str.split, but re.split can:

import re
re.split('[: ]', s)  # ['ab', 'cd', 'ef', 'gh']
