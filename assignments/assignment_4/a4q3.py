# Write a program which contains filter(), map() and reduce(), 
from functools import reduce

input_list = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

filter_result = list(filter(lambda x: 70 <= x <=90, input_list))
map_result = list(map(lambda x: x+10, filter_result))
reduce_result = reduce(lambda x, y: x*y, map_result)

print(filter_result)
print(map_result)
print(reduce_result)
