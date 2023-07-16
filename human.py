class Human:
    humans = []

    def __init__(self, name, age) -> None:
        self.name = name
        self.humans.append(self)
        self.age = age

    @classmethod
    def no_of_humans(cls):
        return len(cls.humans)
    
    @staticmethod
    def shout(n):

        """ shouts Oiii Oii n times """
        for _ in range(n):
            print("Oiii Oii !")

murali = Human("murali", 25)
krishnan = Human("krishnan", 27) 

print(murali.humans)
print(Human.humans)
