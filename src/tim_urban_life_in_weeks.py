"""
1 year = 365 days
1 year = 52 weeks
1 year = 12 months

This is a multi line comment '_'


"""

print("Hi, Hello there, This is Tim Urbans, Life in Weeks !!!")

max_age = 90
current_age = int(input("Please enter your current age: "))
years_left = max_age - current_age
print(years_left)
days_left = years_left * 365
months_left = years_left * 12
weeks_left = years_left * 52

print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months left")

