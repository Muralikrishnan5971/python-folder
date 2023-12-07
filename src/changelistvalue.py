

l = [1, 2, 3, 4, 5, 6]

new = []

new.append(l[len(l) - 1])

for e in range(1, len(l)-1):
    new.append(l[e])

new.append(l[0])   


print(new)


