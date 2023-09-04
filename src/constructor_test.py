class Man:
	def __init__(self, name, age) -> None:
		self.name = name
		self.age = self.calculate_age(age)
	
	def calculate_age(self, age):
		print("function called!!")
		return age + 10

m = Man("murali", 20)

print(m.name)
print(m.age)