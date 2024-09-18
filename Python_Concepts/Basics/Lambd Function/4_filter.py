# filter outa all elements grator than 4
l = [1,2,3,4,5,6,7,8,9,15]
a = filter(lambda x : x >= 4, l)
print(list(a))

# filter all names that dont have s in name
names = ['Shubham','Adarsh','Dev','Harsh','Aryan','soumya']
b = filter(lambda name : 's' not in name and 'S' not in name, names )
c = map(lambda name: 's' in name, names)
print(list(b))
print(list(c))