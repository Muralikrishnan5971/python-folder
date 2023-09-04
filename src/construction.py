
class HomePage:
    
	def __init__(self, location) -> None:
		self.location = location
		self.home_locators()
	
	def __str__(self) -> str:
		return self.location + str(self.locator1) + str(self.locator2)
	
	def home_locators(self):
		self.locator1 = ["left", "right"]
		self.locator2 = ["up", "down"]
	
	def print_hello(self):
		return "Hello"
	
	

hp = HomePage("Office")
print(hp)

def function_one():
	print(hp.print_hello())

def fucntion_two():
	print(hp.print_hello() + "murali")

function_one()
fucntion_two()