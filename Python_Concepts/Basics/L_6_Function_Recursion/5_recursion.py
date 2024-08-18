def show(n):
    if(n==-1): # base case
        return print("Done") 
    print(n)
    show(n-1)

show(int(input("Enter a no. : ")))