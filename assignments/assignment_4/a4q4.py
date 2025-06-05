# Write a program which contains filter(), map() and reduce(), 
# Accept numbers from users and put them into a list
# filter - even numbers
# map - calculate square of filter_result
# reduce - get sum of map_result
from functools import reduce

n = 0
input_list = []
while True:
    n = input()
    if n == 'n':
        break
    input_list.append(int(n))

filter_result = list(filter(lambda x: x%2==0, input_list))
map_result = list(map(lambda x: x*x, filter_result))
reduce_result = reduce(lambda x, y: x+y, map_result)

print(filter_result)
print(map_result)
print(reduce_result)
