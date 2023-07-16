print("Welcome to Rollercoaster !!!")

height = int(input("Please enter your height in cm: "))
bill = 0

if height > 150:
    print("Yay!! You can ride the rollercoaster.")
    age = int(input("Please enter your age in yrs: "))
    if age < 12:
        bill = 5
        print(f"Child tickets are ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}")
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay, Have a free ride on us '_'")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}")

    want_photo = input("Do you want to take photo? Y / N. ")
    if want_photo == "Y":
        bill += 5

    print(f"Your final bill ${bill}")

else:
    print("You need to grow a bit taller to ride, SORRY")