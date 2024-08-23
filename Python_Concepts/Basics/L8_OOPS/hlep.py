def fizzBuzz(A):
    i = 1
    ar = []
    while i <= A:
        if i % 3 == 0 and i % 5 == 0:
            ar.append("FizzBuzz")
        elif i % 3 == 0:
            ar.append("Fizz")
        elif i % 5 == 0:
            ar.append("Buzz")
        else:
                ar.append(i)
        i += 1
    return ar
print(fizzBuzz(5))