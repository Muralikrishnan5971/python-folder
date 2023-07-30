import random
import string

letters = list(string.ascii_letters)
# print(letters)

numbers = list(string.digits)
# print(numbers)

spl_chars = list(string.punctuation)
# print(spl_chars)

print("Welcome to the PyPassword Generator!!")
pg_letters = int(input("How many letters would you like in your password?\n"))
pg_numbers = int(input("How many numbers would you like in your password?\n"))
pg_spl_chars = int(input("How many spl characters would you like in your password?\n"))

pwd_symbols = []
for pg_letter in range(0, pg_letters):
    pwd_symbols.append(random.choice(letters))
    # pwd_symbols += random.choice(letters)   This line also work simailar to the append function

for pg_number in range(0, pg_numbers):
    pwd_symbols.append(random.choice(numbers))

for pg_sql_char in range(0, pg_spl_chars):
    pwd_symbols.append(random.choice(spl_chars))

# print(pwd_symbols)

actual_passwd = ""
for pwd in range(0, len(pwd_symbols)):
    actual_passwd += random.choice(pwd_symbols)

actual_passwd = "".join(actual_passwd)
print(f"Your password is {actual_passwd}")

# same can be done using the random.shuffle function
# random.shuffle(pwd_symbols)
# print(pwd_symbols)