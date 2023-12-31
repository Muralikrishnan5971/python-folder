"""
creating a dict
"""

emp_keys = ["first_name", "last_name", "role"]
emp_vals = None

my_emp = dict.fromkeys(emp_keys, emp_vals)
my_emp['first_name'] = "murali"
my_emp['last_name'] = "krishnan"
my_emp['role'] = "Controller"
print(my_emp)

test_emp = {
	"first_name":"murali",
	"last_name":"krishnan",
	"role":"Controller"
}

print(my_emp == test_emp)

print("************************************** \
	  				***********")
first = "murali"
last = "krishnan"
print("My name is {} {} and i love" 
	  "cinema".format(first, last))

expected_toast_msg = (f"Employee '{first} {last}' "
					   "details has been created successfully")
print(expected_toast_msg)

exp = {'emp_id': 36849, 
 'email_id': 'juliewatson@mailinator.com', 
 'first_name': 'Julie', 
 'last_name': 'Watson', 
 'role': 'Controller', 
 'job_title': 'Controller', 
 'department_type': 'Service', 
 'deapartment': '04 - Mechanical'} 

act = {'emp_id': '36849', 'email_id': 'juliewatson@mailinator.com', 'first_name': 'Julie', 'last_name': 'Watson', 'role': 'Controller', 'job_title': 'Controller', 'department_type': 'Service', 'deapartment': '04 - Mechanical'}