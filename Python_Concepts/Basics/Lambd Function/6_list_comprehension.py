l = [1,2,3,4,5,6,7,8,9,15]

# sq for every number in list
l1 = [i**2 for i in l]
# print(l1)

# all even in range
l3 = [i for i in range(100+1) if i % 2 == 0]
# print(l3)


# cube of all odd in range
l4 = [i**3 for i in range(100+1) if i % 2 != 0]
# print(l4)

# names starting with 's'
names = ['Shubham','Adarsh','Dev','Harsh','Aryan','soumya']
l5 = [name for name in names if name[0] != 's' and name[0] !='S']
print(l5)
l6 = [name for name in names if 'S' in name or 's' in name]
print(l6)