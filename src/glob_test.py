import glob
 
"""
its based on unix path expansion rule 
"""
print(glob.glob("????mobile.py"))
print(glob.glob("????.py"))  # list all filenames with 4 characters and end with .py

# absolute wildcard

print(glob.glob("add*"))
print(glob.glob("*.py"))

"""
It will match everything in front of . and it should contain a . and it will match everything after the .  
"""
print(glob.glob("*.*"))

# lists all file that start with 'f'
print(glob.glob("[f]*"))

# lists all file that start with (first chracter) 'f' and 'l'
print(glob.glob("[fl]*"))

#lists all file that start with (first chracter) 'f', 'l' and 'b'
print(glob.glob("[flb]*"))

# lists all file EXCEPT that start with (first chracter) 'f', 'l' and 'b'
print(glob.glob("[!flb]*"))

print("*" * 50)

# searching for a match recursively
print(glob.glob("**/*.css"))

print(glob.glob("**/[d]*.txt"))

