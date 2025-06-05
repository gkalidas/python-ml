# Write a program which accepts a number from user and return addition of it's factors.

print("Enter the number: ")
no = int(input())

sum = 0
i = 1

while (i <= (no/2)):
    if no%i == 0:
        # print("Factors are ", i)
        sum += i
    i+=1

print("Sum is ", sum)
