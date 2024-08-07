list = []
n = int(input("no. of elements "))

for i in range(n):
    ele = int(input())
    list.append(ele)

print(list)

copy_list = list.copy()
copy_list.reverse()

print("Palindrome" if list == copy_list else "Not Palindrome")