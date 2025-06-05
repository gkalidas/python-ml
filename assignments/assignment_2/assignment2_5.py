# Write a program to accept a no from user and check whether it is a prime or not

no = int(input())

i = 2

while (i<= no/2):
    if i%no==0:
        break
    i += 1
if (i > no/2):
    print(f"{no} is a prime number")
else:
    print(f"{no} is not a prime no.")