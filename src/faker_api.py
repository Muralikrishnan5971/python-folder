from faker import Faker

f = Faker("en-US")

print((f.first_name()).lower())