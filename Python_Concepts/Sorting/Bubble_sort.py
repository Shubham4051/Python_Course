# ar = [5,3,7,3354,574,57,0,0,75,2,0,9999,26]
ar = [4,6,8,3,2,5,7,8,9]

c = 0

for i in range(len(ar)-1):
    for j in range(0,len(ar)-1-i):
        if ar[j] > ar[j+1] :
            ar[j], ar[j+1] = ar[j+1], ar[j]
            c += 1
        print(ar, c, ar[j], ar[j+1])
    print()

print(ar)
# def bubble(list_a):
#     c = 0
#     indexing_length = len (list_a) - 1
#     sorted = False
#     while not sorted:
#         sorted = True
#         for i in range(0, indexing_length):
#             if list_a[i] > list_a[i+1]:
#                 sorted = False
#                 list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
#                 c += 1
#     return list_a,c
# print(bubble([4,6,8,3,2,5,7,8,9]))