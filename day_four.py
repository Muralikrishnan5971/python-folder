# Randomisation
import random
import test_module

# generates random numbers including 200 and 350
random_integer = random.randint(200, 350)
print(random_integer)

# generates random folat numbers between 0 and 1 but not including 1
random_float = random.random()
print(random_float)

# we can expand the range of random float numbers by multiplying a number
# this prints 0.00000.... to 4.999999..... randomly but not 5
print(random_float * 5)

random_number = random.randint(1, 5)
print(random_number)


print(test_module.get_the_value_of_pi())
