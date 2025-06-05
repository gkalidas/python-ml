# Create a module named Arithmetic which contains
# four functions, as add(), sub(), mul(), div()
# All of them will accept two parameters as numbers and perform oprations
# Write one python program which will call all the functions from 
# Arithmetic module by accepting parameters from user

from Arithmetic import Arithmetic

no_1 = int(input())
no_2 = int(input())

print(Arithmetic.add(no_1, no_2))
print(Arithmetic.sub(no_1, no_2))
print(Arithmetic.mul(no_1, no_2))
print(Arithmetic.div(no_1, no_2))
