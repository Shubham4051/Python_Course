def factorial(x):
    '''
    This program is made to use recursion for the factorial of a no.
    inp = a
    out = a
    created by - Shubham
    last edit - 15/10/2024
    '''
    if x == 1:
        return 1
    else :
        return x * factorial(x-1)

print(factorial(5))