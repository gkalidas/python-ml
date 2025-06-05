# Write a program which accepts one number from user and return it's factorial.

no = int(input())

factorial = 1
while(no > 0):
    factorial = factorial * no
    no -= 1

print("Factorial of given number is ", factorial)
