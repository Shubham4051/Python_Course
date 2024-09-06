import random

print("Let's Start the game... ")

x = random.randint(1,100)
n = int(input("Enter a number... "))
c = 1

while n != x:    
    if n > x:
        print("Try a smaller value...")
        n = int(input())
        c+=1
    else:
        print("Try a bigger value...")
        n = int(input())
        c+=1

print("Congrats... You tried", c, "times")



# for auto play 

# print("Let's Start the game... ")

# x = random.randint(1,100)
# n = random.randint(1,100)
# c = 1

# while n != x:    
#     if n > x:
#         print(n,"Try a smaller value...")
#         n = random.randint(1,n)
#         c+=1
#     else:
#         print(n,"Try a bigger value...")
#         n = random.randint(n,100)
#         c+=1

# print(n,"Congrats... You tried", c, "times")
