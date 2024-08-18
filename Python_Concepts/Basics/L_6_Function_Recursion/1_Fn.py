# fn define
def calc_sum(n1,n2): # parameters
    s = n1 + n2
    # return n1 + n2
    print(s)

a,b = map(int, input("Enter 2 no. : ").split())
# print(calc_sum(a,b))
calc_sum(a, b) # fn call, arguments