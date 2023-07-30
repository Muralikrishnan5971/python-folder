print("Hi, This is a Body Mass Index Calculator - BMI")

weight = int(input("Please enter yout weight in kg: "))
height = float(input("Please enter yout height in mts: "))

bmi = round(weight / (height ** 2))

# using format strings
# print("Your body mass index for weight {} and height {} is {}".format(weight, height, int(bmi)))

# using f-strings
print(f"Your body mass index for weight {weight} and height {height} is {bmi}")

if bmi <= 18.5:
    print("You are UNDERWEIGHT")
elif bmi <= 25:
    print("You weigh NORMAL")
elif bmi <= 30:
    print("You are OVERWEIGHT")
elif bmi <= 35:
    print("You are OBESE")
else:
    print("You are CLINICALLY OBESEcle")
