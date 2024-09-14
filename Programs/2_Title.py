# n = 'Shubham'
# print(n[::-1])

# # name,age,sex = input().split(maxsplit=2)
# # print(name,age,sex,sep='\n')
# age = int(input("Age : "))
# name = input('Name : ')
# sex = input("Sex : ")
# print("Hola Amigo ! I am {}, and I am {} years old. And sex --{} ".format(name,age,sex))


x = input("Enter the string you want to add as a title. : ")
print(x)

line = x.split()
# print(line)

done =[]

for i in line:
    done.append(i.capitalize())
print(done)

done = " ".join(done)
print(done)

# # Bonus Name from email

# mail = "shubhamadarsh@gamil.com"
# f = mail.find('@')
# print(mail[:f])