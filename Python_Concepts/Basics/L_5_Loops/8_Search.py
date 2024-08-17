sq = [1,4,9,16,25,36,49,64,81,100,1,4,9,16,25,36,49,64,81,100]
# print(type(sq))
for no in sq:
    print(no)

n = int(input("Enter a no. to searh in list "))

i = 0
for no in sq:
    if no == n :
        print(no, "found at index",i )
        break
    i += 1