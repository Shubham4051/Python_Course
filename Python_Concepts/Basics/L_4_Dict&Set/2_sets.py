set1 = {1,2,2,2,3,3,4,"Hello", "city", "City", "city", 1,2,3,4}

# print(set1.pop())

print(len(set1))
print(set1)
print(type(set1))

# empty_set = set()
# print(type(empty_set))

set1.add((5,6,7))
set1.add(8)
set1.add(9)
set1.remove("City")

print(set1)
print(len(set1))

# set1.clear()
# print(len(set1))

set2 = {"Hello", 7, 8, 9,10, "Racers", "Go"}

print(set1.union(set2))
print(set1.intersection(set2))