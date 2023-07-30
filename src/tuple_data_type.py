"""
tuple is very much similar to list data type, except it is immutable,
whereas list are NOT immutable.

"""

a = (3, 45, "number", 0,524245)
print(a)

dic = {1:"murali", "lastname":"krishnan", 3:4223324, 4:0.242342342}
print(dic)
print(dic["lastname"])

employee = {}
print(employee)

employee["firstname"] = "murali"
employee["lastname"] = "krishnan"
employee["job-title"] = "QA Engineer"
employee["age"] = "25"
employee["department"] = "QA"

print(employee)
