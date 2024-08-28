'''
1. Let us say your expense for every month are listed below,
i. January - 2200
ii. February - 2350
iii. March - 2600
iv. April - 2130
v. May - 2190
Create a list to store these monthly expenses and using that find out,
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list
based on this
'''
exp = [2200, 2350, 2600, 2130, 2190]

print(exp)

a1 = exp[1] - exp[0]

a2 = exp[0] + exp[1] + exp[2]

a3 = False
c = 0
for i in exp:
    if i == 2000:
        a3 = True, c
        c += 1 

a4 = exp.append(1980)

exp[3] = exp[3] - 200

print(a1, a2, a3, a4, exp)