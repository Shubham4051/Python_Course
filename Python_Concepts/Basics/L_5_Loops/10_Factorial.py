n = int(input("Enter a no to find sum and factorial : "))
sum = 0
fact = 1
for i in range(1,n+1,1):
    sum += i
    fact *= i

print("sum = ", sum, "\nfactorial = ", fact )