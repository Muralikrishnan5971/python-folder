print("Welcome to the Love Calculator !!!")
name1 = input("Please enter your name: \n")
name2 = input("Please enter your partner name: \n")

combined_names = name1 + name2
combined_names_in_lower_case = combined_names.lower()
t = combined_names_in_lower_case.count("t")
r = combined_names_in_lower_case.count("r")
u = combined_names_in_lower_case.count("u")
e = combined_names_in_lower_case.count("e")
true = t + r + u + e

l = combined_names_in_lower_case.count("l")
o = combined_names_in_lower_case.count("o")
v = combined_names_in_lower_case.count("v")
e = combined_names_in_lower_case.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your Love score is {love_score}, you go together like coke and mentos !!!")
elif love_score >= 40 and love_score <= 50:
    print(f"Your Love score is {love_score}, you are alright together '_'")
else:
    print(f"Your Love score is {love_score}")

