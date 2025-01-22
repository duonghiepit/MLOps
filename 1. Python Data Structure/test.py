l1 = [1, 2, 3, 1, 2, 3, 3, 4, 5]

i=0
while i<len(l1):
    if l1[i] == 1:
        l1.remove(l1[i])
    i+=1

print(l1)