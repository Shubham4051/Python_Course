def sum(func,l):
    res = 0
    for i in l:
        if func(i):
            res = i + res
    return res        

l = [1,2,3,4,5,6,7,8,9,15]
x = lambda x:x % 2 == 0
y = lambda y : y % 2 != 0
z = lambda z : z % 3 == 0

print(sum(x,l))
print(sum(y,l))
print(sum(z,l))