"""
Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1

"""

print("Welcome to Python pizza deliveries !!!")
size = input("What soze of pizza do you want ? S, M or L ")
add_pepperoni = input("Do you want pepperoni ? Y / N ")
add_chesse = input("Do you want extra chesse ? Y / N ")

bill = 0
pepperoni = 0

"""
if size == "S":
    bill = 15
    print(f"Small size pizza costs ${bill}")
    if add_pepperoni:
        print("Pepperoni for small size pizza costs $2")
        bill += 2
    if add_chesse:
        print("Extra cheese for pizzas costs $1")
        bill += 1   
    print(f"Your total bill costs ${bill}")
elif size == "M":
    bill = 20
    print(f"Medium size pizza costs ${bill}")
    if add_pepperoni:
        print("Pepperoni for medium size pizza costs $3")
        bill += 2
    if add_chesse:
        print("Extra cheese for pizzas costs $1")
        bill += 1 
    print(f"Your total bill costs ${bill}")
elif size == "L":
    bill = 25
    print(f"Large size pizza costs ${bill}")
    if add_pepperoni:
        print("Pepperoni for medium or large size pizza costs $3")
        bill += 3
    if add_chesse:
        print("Extra cheese for pizzas costs $1")
        bill += 1   
    print(f"Your total bill costs ${bill}")
else:
    print("Bro.....do you even know alphabets |-|")
"""

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if add_chesse == "Y":
    bill += 1

print(f"Your final bill is ${bill}")
