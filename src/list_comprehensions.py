
def add_ten(num):
    return num + 10

nums = [x for x in range(1, 15)]
print([ x * 5 for x in nums ])
print([ add_ten(x) for x in nums if x%2 == 0])

strs = ['vim', 'is', 'awesome', 'with', 'python']
print([ s.upper() for s in strs ])
print([ s.upper() + "*-*"  for s in strs ])


dicts = [{'name':'murali'},{'name':'krishnan'}]
print([ x['name'] + "python"  for x in dicts ])

# using if else statements in list comprehensions

# -> if else statement to the left of for loop (changes the values in list
# based on the given expression ***CHANGE VALUES***

nums = [x for x in range(1, 15)]
print([ x * 10 if x % 2 == 0 else x for x in nums ])
print([ x * 10 if x % 2 == 0 else x * 5 for x in nums ])

# -> if else statement to the right of the for loop (filters out the values in
# the list based on the given expression ***FILTERS OUT VALUES***

sentence = "You are a character, doesn't mean you have character"

def is_vowel(l):
    vowels = "aeiou"
    return l.isalpha() and l.lower() in vowels

print([ i + " is a consonant" for i in sentence.replace(" ", "") if not is_vowel(i) ]








"""
List Comprehension
-----------------

Always returns a list
For any list comprehension to work we need a expression and a iterable.

[expresion for i in iterable]

"""
