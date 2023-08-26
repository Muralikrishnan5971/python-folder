qoute = 'Give everyman thy ear, but few thy voice'
print(qoute[0])
print(qoute[1:3])
print(qoute[-3:-1])
print(qoute[-3:])

x = qoute.split()
print(x)

print(x[-3] + " " + x[3] + " " + x[2] + " " + x[-1])

print(x.index("thy"))

import this

"""
The idea of slicing is simple. We carve out a subsequence (called a 'slice') from a 
sequence by defining the start and end indices. While indexing retrieves only a single 
element, slicinh retrieves a whole subsequence within an index range.

word[i:j] returns a substring starting from index i (included) and ending in index j (excluded).
"""

print("*" * 100)

x = 'universe'
print(x[2:4])

"""
Advanced slicing notation consists of three arguments [start:end:step]
"""
print('python'[:5:2])

print(x[2::2])

"""
Overshooting indices in slicing. Slicing is robust even if the end index shoots over the maximal
sequence index. But rememnber that nothing unexpected happens if slicing overshoots sequence indices.
"""
word = 'milkywaygalaxy'
print(word[4:50])

print("*" * 100)

s = 'sunshine'
print(s[1:5:2] + s[1:5:1])

"""
What does it mean to skip slicing indices. ex: s[::2] ?
The python interpreter assumes certain default values for s[start:stop:step]. We can tell the 
interpreter to use the default values by simply skipping the value(s) before and after values. 

For most simple cases the default values are start=0, stop=len(s), and step=1 

"""
name = 'muralikrishnan'
print(s[::] == s[0:len(name):1])

series = 'Game of Thrones'
print(series[:-2])
print(series[4:])
print(series[:])

"""
The below three slice produces the same result, but the first two is considered bad style.
first slice has a redundant colon
second slice is even worse as it contains not only a redundant colon, 
but also a redundant default value.

As a rule of thumb, we should always avoid redundant code.
"""
qoute = 'O brother where art thou?'
print(word[::])
print(qoute[::1])
print(qoute[:])

"""
Negative step size -- A negative step index indicates that we are not slicing from left to right,
but from right to left. Hence start index should always be greater than or equal to end index.
Otherwise, the resulting sequence is empty.

"""
name = 'muralikrishnan'
print(name[5:1:-1])
print(name[1:5:-1])

qoute = 'Oh gravity, thou art a heartless bitch'
print(qoute[9:2:-1][::-1])

"""
when we are using negative indices, the default values of start and stop also gets changed.

s='example'
start=len(s)-1
stop=-len(s)-1
"""
qoute = 'you shall not pass!'
print(qoute[len(word):0:-1])
print(qoute[len(word):0:-1] == qoute[::-1])

print(qoute[len(qoute)-1:-len(qoute)-1:-1] == qoute[::-1])
print("*" * 100)

""" <--- List slicing ---> """
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l[2:])
print(l[::-2])

"""
Why is the last index excluded from the slice ?

In python, as in many other programming languages when defining an interval [start, end], 
the end index is not included in the subsequence.

The last index is excluded from the slice because of language consistency.
ex: the range function also does not include the end index.

"""
"""
Is the slice sub string an alias of the original substring 
(i.e., does the resulting object refer to the same object in memory ?)

Strings are immutable in python, they cannot be changed. Thus applying a slice operation to a
string, the interpreter will create a new string.

The same holds for list. Slicing creates a copy of the list, we do not have to worry about 
accidentally modifying the original sequence.

"""
directors = ['tarantino', 'wes anderson', 'paul thomas anderson', 'wong kar wai', 'koreeda']
western_directors = directors[:2]
western_directors.remove('wes anderson')
print(western_directors)
print("*" * 100)

""" Slice Assigning """

l = [1, 2, 3, 4, 5, 6]
l[:3] = [11, 22, 33]
print(l)

m = [22, 33, 55, 66, 77]
# m[::2] = [1, 2]
print(m) 
"""
This will throw a ValueError. The sliced list will have three elements.
We have assigned only two elements in the slice assignment.
Hence causes the Value Error
"""
""" 
Can we use slice assignments for Strings ?
NO, Because Strings are Immutables.
"""
print("*-" * 150)
""" PUZZLES """

s = "All that glitters is not gold"
print(s[9:-9])
print(s[::10])
print(len(s))
default_start = 28  # 29 - 1
default_end = -30 	# -29 - 1 
print(s[28:-30:-1])
print(s[:-4:-1])

x = list('universe')
print(x)
print(x[2:4])
print(x[2::2])
print(x[4:50])

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[1:5:2] + lst[1:5:1])

lst = [2, 4, 6, 8, 10, 12]
print(lst[:-2] + lst[4:1])
print(lst[:])

lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(lst[::])	#bad
print(lst[::1])	#bad
print(lst[:])

word = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(word[9:1:-1][::-1]) #****

