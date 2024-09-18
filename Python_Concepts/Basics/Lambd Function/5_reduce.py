import functools
l = [52,89,48,56,27,46,96,75]

# reduce to sum
print(functools.reduce(lambda x,y : x+y, l))
# print(sum(l))

# reduce to largest number
print(functools.reduce(lambda x,y : x if x > y else y, l))

# reduce to smallest number
print(functools.reduce(lambda x,y : x if x < y else y, l))