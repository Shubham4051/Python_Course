def binary_searh(arr,x):
    l = 0
    h = len(arr)-1
    while l <= h:
        mid = l + (h - l) //2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            h = mid-1
        else:
            l = mid+1
    return None

arr = [1,2,3,4,5,6,7,8,9,99,999,7,18424,64566645]
x = 7
print(binary_searh(arr, x))