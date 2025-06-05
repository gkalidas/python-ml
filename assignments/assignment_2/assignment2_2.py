"""
Write a program which accepts one number from user and print below patter
i/p = 5
output = starts 5rows * 5columns
*       *       *       *       *
*       *       *       *       *
*       *       *       *       *
*       *       *       *       *
*       *       *       *       *
"""

no = int(input())
i, j = 0, 0
for i in range(no):
    print()
    for j in range(no):
        print("*", end = "\t")
