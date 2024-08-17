lt = (1,4,9,16,25,36,49,64,81,100)
print(lt)

n = int(input("Enter the no. to search for : "))

c = 0
while c < len(lt) :
    
    if lt[c] == n :
        print(lt[c], "Found at index", c)
        break
    else:
        print("Finding .....")
    c += 1  