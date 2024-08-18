def pr_fct(no):
    c = 1
    for i in range(1,no+1):
        c *= i
        print(c, end=', ')
    return c

n = int(input("Enter a no. : "))
print("Final ans is = ",pr_fct(n))