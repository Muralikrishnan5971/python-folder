print("Adding all even numbers from 1 to 100")
sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum += number
print(f"Sum of all even numbers from 1 and 100 is: {sum}")

sum = 0
for number in range(2, 101, 2):
   sum += number
print(f"Sum of all even numbers from 1 and 100 is: {sum}")