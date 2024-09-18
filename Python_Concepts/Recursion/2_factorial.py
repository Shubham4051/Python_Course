def factorial(x, d):
    {'''
    This program is made to use recursion for the factorial of a no.
    inp = a
    out = a
    created by - Shubham
    last edit - 15/10/2024
    '''}
    if x in d:
        return d[x]
    else :
        d[x] = x * factorial(x-1,d)
        return d[x]

d = {0:1, 1:1}
print(factorial((int(input())),d))

print(d)