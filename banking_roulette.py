import random

input_name = input("Give me everybody's names, separated by a comma. ")
name_list = input_name.split(", ")
name_list_length = len(name_list)
random_choice = random.randint(1, name_list_length - 1)
person_who_will_pay = name_list[random_choice]
print(person_who_will_pay + " is going to buy the meal today!")

# the above code can be also implemented using random.choice()
person_who_will_pay = random.choice(name_list)
print(person_who_will_pay + " is going to buy the meal today!")