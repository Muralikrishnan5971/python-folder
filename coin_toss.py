import random

# randint function generated random integer inclusive of both numbers (0 and 1)
random_side = random.randint(0, 1)

if random_side == 1:
    print("Heads.")
else:
    print("Tails")
