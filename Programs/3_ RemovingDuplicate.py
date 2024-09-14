import random

lt = []
for i in range(100):
    lt.append(random.randint(0,100))
print(sorted(lt),len(lt))

lt2 = []

for i in lt:
    if i not in lt2:
        lt2.append(i)
print(sorted(lt2), len(lt2))


