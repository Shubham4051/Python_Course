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

def quick_sort(arr):
    if len(arr) > 1:
        pivot = arr.pop()
    else:
        return arr
    
    arr_big = []
    arr_small = []

    for items in arr:
        if items < pivot:
            arr_small.append(items)
        else:
            arr_big.append(items)
    new_arr = quick_sort(arr_small) + [pivot] + quick_sort(arr_big)
    return new_arr

print(quick_sort([4,6,8,3,2,5,7,8,9]))