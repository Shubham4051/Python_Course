
def mul(x,y):
    '''
    This program is made to use recursion for the multiplacation of two numbers
    inp = a,b
    out = a*b
    created by - Shubham
    last edit - 15/10/2024
    '''
    if y == 1:
        return x
    else:
        return x + mul(x,y-1)

print(mul.__doc__)

a,b = map(int, input().split())
print(mul(a,b))