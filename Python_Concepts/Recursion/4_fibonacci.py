def memo_fib(x,d):
    if x in d:
        return d[x]
    else:
        d[x] = memo_fib(x-1,d) + memo_fib(x-2,d)
        return d[x]
    

x = int(input())
d = {0:0, 1:1}
print(memo_fib(x,d))

# inefficient code as takes too much time
# def fib(x):
#     if x == 0 or x== 1:
#         return 1
#     else:
#         return fib(x-1) + fib(x-2)
# print(fib(3)) 