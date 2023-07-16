class Square:
    def __init__(self, side) -> None:
        """
        __init__ is a dunder method that INITialises the instance.

        To create a square, we need to know the lenght of its side,
        So that will be passed as argument later, when we create an instance. eg: Square(4)

        To make sure the instance knows its own side length,
        we save it with self.side = side
        """
        print("Inside INIT")
        self.side = side

s = Square(5)
