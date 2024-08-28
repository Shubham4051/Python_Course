# # ar = [5,3,7,3354,574,57,0,0,75,2,0,9999,26]
ar = [4,6,8,3,2,5,7,8,9]

idx = len(ar)
c = 0

for i in range(idx):
    min_idx = i
    for j in range(i+1, idx):
        if ar[j] < ar[min_idx]:
            min_idx = j
            c += 1
            print(ar, c)
        print()
    if min_idx != i:
        ar[min_idx], ar[i] = ar[i], ar[min_idx]
print(ar)

# def selection_sort(arr):
#     """
#     Sorts the input array in ascending order using selection sort.
#     """
#     n = len(arr)
#     c = 0
#     for i in range(n):
#         # Find the minimum element in the remaining unsorted portion
#         min_idx = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#                 c += 1
#                 print(arr,c)

#         # Swap the minimum element with the current position
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

# # Example usage
# my_array = [4, 6, 8, 3, 2, 5, 7, 8, 9]
# selection_sort(my_array)
# print("Sorted array:", my_array)