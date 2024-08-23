# n = int(input())
# for i in range(n):# for sq
#     print('#'*n)

# print()

# for i in range(1,n+1,1): # triangle
#     print('#'*i)

# print()

# p = n-1
# for i in range(1,n+1,1): # triangle
#     print(' '*p,'#'*i)
#     p -= 1

# print()

# q = n-1
# for i in range(1,n+1,1): # triangle
#     print(' '*q,'# '*i)
#     q -= 1

def star_pattern(n):
    # YOUR CODE GOES HERE
    for i in range(1, n + 1):
        for j in range(n - i):
            print("#", end="")
        for k in range(1, 2*i):
            print("*", end="")
        print()
star_pattern(5)