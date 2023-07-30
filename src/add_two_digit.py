"""
Write a program that adds the digits in a 2 digit number. 
e.g. if the input was 35, then the output should be 3 + 5 = 8\
"""

two_digit_num = input("Please enter a two digit number: ")
# str_two_digit_num = str(two_digit_num)
print(type(two_digit_num))
digit_1 = int(two_digit_num[0])
digit_2 = int(two_digit_num[1])

print(digit_1 + digit_2)