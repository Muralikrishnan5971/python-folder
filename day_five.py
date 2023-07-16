

fruits = ["Apple", "Pear", "Orange"]

for fruit in fruits:
    print(fruit + " Juice")


for number in range(1, 10):
    print(number)

# the range function by default steps once,
for number in range(1, 10, 1):
    print(number)

# sum numbers from1 to 100
sum = 0
for number in range(1, 101):
    sum += number
print(f"The sum of numbers from 1 to 100 is {sum}")