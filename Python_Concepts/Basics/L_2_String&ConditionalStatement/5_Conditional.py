# print("Vote")
# age = int(input())
# if(age >= 18):
#     print("Yes")
# else:
#     print("No")

'''
if, elif, else
'''
print("Greater Number - 3")
n1, n2, n3 = map(int, input().split())
if(n1 >= n2 and n1 >= n3):
    print(n1)
elif(n2 >= n3):
    print(n2)
else:
    print(n3)