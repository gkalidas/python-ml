from functools import reduce

n = 0
input_list = []
while True:
    n = input()
    if n == 'n':
        break
    input_list.append(int(n))

def find_max(a, b):
    print("a, b", a,b)
    if a>b:
        return a
    else:
        return b

filter_result = list(filter(lambda x: x%2==0, input_list))
map_result = list(map(lambda x: x*2, filter_result))
reduce_result = reduce(find_max, map_result)

print(filter_result)
print(map_result)
print(reduce_result)
