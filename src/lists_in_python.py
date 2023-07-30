# list can have multiple data types

l = ["apple", "grape", 3 , True, 3434.23423]
print(l)
print(l[0])
print(l[3])
print(l[4])

# negative indexes
print(l[-1])
print(l[-2])
print(l[-3])
print(l[-4])
print(l[-5])

# list appending

l[3] = False
l[1] = "murali"

# append function adds a single item to the end of the list
l.append("krishnan")
l.append(252453)

print(l)

l.extend(["python", 3, "is", 45423432, "Awesome"])

print(l)

# nested lists

m = ["orange", "appple", "papaya"]
n = ["carrot", "beetroot", "tomato"]

l = [m, n]

print(l)
print(l[0][2])
print(l[1][1])
