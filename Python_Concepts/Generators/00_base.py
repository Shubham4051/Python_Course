def demo_gen():
    yield " S1"
    yield 's2'
    yield "s3 "
    yield "s4 "
    yield "s5 "
    yield "s6 "

generator = demo_gen()

print(next(generator))
print(next(generator))

for _ in generator: # loop continues from where left
    print(_)
