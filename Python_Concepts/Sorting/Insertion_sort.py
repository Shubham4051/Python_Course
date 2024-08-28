ar = [5,3,7,3354,574,57,0,0,75,2,0,9999,26]

# ar = [4,6,8,3,2,5,7,8,9]
c = 0

for i in range(1, len(ar)):
    while ar[i] < ar[i-1] and i > 0:
        ar[i], ar[i-1] = ar[i-1], ar[i]
        i = i-1
        c += 1
print(ar,c)