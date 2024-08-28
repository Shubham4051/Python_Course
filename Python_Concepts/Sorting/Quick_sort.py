# def quick_sort(arr):
#     c = 0
#     length = len(arr)
#     if length <= 1:
#         return arr
#     else:
#         pivot = arr.pop()
    
#     ele_big = []
#     ele_small = []

#     for item in arr:
#         if item < pivot:
#             ele_small.append(item)
#         else :
#             ele_big.append(item)
#     return quick_sort(ele_small) + [pivot] + quick_sort(ele_big)


# print(quick_sort([4,6,8,3,2,5,7,8,9]))

