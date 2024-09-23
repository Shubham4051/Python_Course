def sq_gen(end):
    for i in range(1,end+1):
        yield i**2 

generator = sq_gen(10)
print(next(generator))
print(next(generator))
print(next(generator))


print('Continue in loop ')

for _ in generator:
    print(_)