info = {
    'Name':'Shubham', 'Age':24, 'Sex':'Male', 'Occupation':'Fresh'
}

d1 = {key:value for key, value in info.items() if len(key) > 3}
print(d1)

nums = [1,2,3,4,5,6,7,8,9,88,99]
d2 = {item:item**2 for item in nums}
d3 = {item:item**2 for item in nums if item % 2 == 0}
print(d2)
print(d3)