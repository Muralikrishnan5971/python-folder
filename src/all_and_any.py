"""
In python, when we need to check, if any item or all items in an iterable evaluate to True? 
functions any() and all() come into handy.

You can call bool() on any Python object to get its truth value. 

"""
# truth value of None is False
print(bool(None))

# truth value of an empty string ("") is False
print(bool(""))

# truth value of an empty list ([]) or any iterable is False
print(bool([]))

# truth value of 0 {int (0), float (0.0) and complex (0j)} is False
print(bool(0))
print(bool(0.0))
print(bool(0j))

list_1 = [0,0,0,1,0,0,0,0]
print(any(list_1)) # any(a list with at least one non-zero entry) returns True
print(all(list_1)) # False

list_2 = ["","","code more"]
print(any(list_2)) # True

list_3 = ["","",""]
print(any(list_3)) # any(a list of empty strings) returns False

list_4 = ['car', 'bike', 'boat']
print(all(list_4))	# True

# Checking for digit in a string using list conprehension and any function
text = 'djf34lfss923sdkjf34'
is_digit_present = [x.isdigit() for x in text]
print(is_digit_present)
print(any(is_digit_present))
print(all(is_digit_present)) # False
print( "=" * 100)

# Checking for alphabets in a string using list conprehension and any function
is_alphabet = [x.isalpha() for x in text]
print(is_alphabet)
print(any(is_alphabet))
print(all(is_alphabet)) # Flase

"""
now we can combine multiple conditions into a iterable and check for OR and AND if conditions

"""
condition1 = True
condition2 = ""
condition3 = 1
conditions = [condition1, condition2, condition3]

if any(conditions):
    print("one of the condition is true")
