
a = 1
while a < 11:
    a+=1
    print(a,id(a))

b = a
c = b
print(id(b), id(c))
if c == a:
    print(True)

del(a,b,c)
print(id(2))