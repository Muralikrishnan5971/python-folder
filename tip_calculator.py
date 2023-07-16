# pylint: disable=consider-using-f-string

"""
If the bill was $150.00, split between 5 people, with 12% tip
Each person should pay (150.00 / 5) * 1.12 = 33.6
Round the decimals to two decimla points = 33.60

for 150 bill amt, 12 % tip and 7 people split, 
we get 33.6 and not 33.60 which is formatting problem in pyhton rather a math problem
https://docs.python.org/3/tutorial/floatingpoint.html


"""


print("Welcome to the tip calculator!")
bill_amount = float(input("Please enter the bill amount? $"))
tip_percentage = int(input("What percentage of tip would you like to give? 10, 12 or 15 "))
no_of_people_to__split = int(input("How many people to split the bill? "))
tip_amt = bill_amount * (tip_percentage / 100)
total_bill = bill_amount + tip_amt
bill_per_person = total_bill / no_of_people_to__split
print(round(bill_per_person, 2))
print(f"Each person should pay: ${round(bill_per_person, 2)}")

bill_per_person = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${bill_per_person}")
