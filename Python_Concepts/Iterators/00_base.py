a = (1,2,3,4,5)
iterator1 = iter(a)
iterator2 = iter(iter(a))
iterator3 = iter(iterator1)
iterator4 = iter(iterator2)

# print(id(iter))
print(id(iterator1))
print(id(iterator2))
print(id(iterator3))
print(id(iterator4))


print(iterator1)
print(iterator2)
print(iterator3)
print(iterator4)
