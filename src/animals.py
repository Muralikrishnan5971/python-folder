class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("Hi my name is", self.name, "and I am", self.age, "years old!")

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight
    
    def talk(self):
        print("RrrrrrRoughhh....")


class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def talk(self):                 # overriding 
        print("meeeeowwww....")

larry = Cat("Larry", 9, "balck with ash spots")
larry.speak()
larry.talk()
    



















t = Dog("tiger", 9)
t.speak()
print(t.age)
t.change_age(55)
t.speak()
print(t.name)
print(t.age)
t.add_weight(63)
print(t.weight)

print( "*" * 50)

m = Dog("mani", 4)
m.speak()
print(m.age)
m.change_age(44)
m.speak()
print(m.name)
print(m.age)

