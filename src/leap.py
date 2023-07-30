

year = int(input("Please enter your year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a LEAP YEAR !!!")
        else:
            print(f"The year {year} is NOT a LEAP YEAR !!!")
    else:
        print(f"The year {year} is a LEAP YEAR !!!")
else:
    print(f"The year {year} is NOT a LEAP YEAR !!!")
