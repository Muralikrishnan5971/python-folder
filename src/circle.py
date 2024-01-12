import math

class Circle:
    def __init__(self, radius) -> None:
            if radius < 0:
                  raise ValueError("Radius can only be positive")
            self.radius = radius
            self.category = 'shapes'

    def area(self):
          assert self.radius > 0, "Positive radius value expected"
          return math.pi * self.radius ** 2

r = 5
c = Circle(r)
print(f"Area of a circle with radius {r} is", c.area(),
      "which belongs to the category of", c.category)
