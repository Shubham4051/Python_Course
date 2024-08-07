sec = [1, 'a', 3, 'c', 5, 6, 7, 8]
print(sec)
print(len(sec))
print(sec[0])
print(sec[-1])
sec[1] = 'Shubham'
print(sec)
print(sec[4:])
list = ["gogo", "lol", 999, 10156]
# Append
emp = []
emp.append(list)
emp.append(sec)
print(emp)
emp2 = sec + list
print(emp2)

# Sort
set = [3, 55, 90, 4258, 9, 7, 1, 0, 000, -6]
set.sort()
print(set)
set.sort(reverse=True)
print(set)

# Reverse
emp2.reverse()
print(emp2)

# Insert
set.insert(0, "Shubham Adarsh")
print(set)

# Remove by elemnts
set.remove(-6)
print(set)

# Pop by index
set.pop(0)
print(set)