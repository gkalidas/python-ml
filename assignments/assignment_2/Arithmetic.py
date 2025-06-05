# Create a module named Arithmetic which contains
# four functions, as add(), sub(), mul(), div()
# All of them will accept two parameters as numbers and perform oprations
# Write one python program which will call all the functions from 
# Arithmetic module by accepting parameters from user

class Arithmetic:
    def add(a:int, b:int):
        return a + b
    
    def sub(a:int, b:int):
        if a < b:
            return b - a
        return a - b

    def mul(a:int, b:int):
        return a * b

    def div(a:int, b:int):
        return a / b
