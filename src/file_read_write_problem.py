"""
Read the file, store all the lines in a list
Reverse the list
Write the list into the same file
"""

with open('read_write.txt', 'r') as f:
    lines = f.readlines()
    reversed(lines)
    with open('read_write.txt', 'w') as w:
        for line in reversed(lines):
            w.writelines(line)


# print(lines, len(lines))
# print(list(reversed(lines)))
name = "muralikrishnan"
reversed(name)
print(name)


