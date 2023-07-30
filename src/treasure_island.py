def print_ascii_art(art_file):
    """
    Read and print ASCII Art
    """
    _f = open(art_file, "r", encoding="UTF-8")
    print(''.join([line for line in _f]))
    print("\n")

print_ascii_art("treasure_island_ascii_art.txt")

print("Welcome to Treasure Island. Your mission is to find the treasure.")
response1 = input('You\'re at a cross road. \nWhere do you want ot go ? Type "left" or "right" \n').lower()

if response1 == "right":
    print("You have fell into a hole, GAME OVER !!!")
else:
    response2 = input('''You have come to a lake.
    There is an island in the middle of the lake
    Type 'wait' to wait for a boat. Type 'swin' to swin across.''').lower()
    if not response2 == "wait":
        print("You were attacked by a trout, GAME OVER !!!")
    else:
        response3 = input('''You have arrived at the island unharmed.
        There is a house with 3 doors.
        One red, one yellow and one blue.
        Which colour do you choose ?''').lower()
        if response3 == "red":
            print("You are burned alive, GAME OVER !!!")
        elif response3 == "blue":
            print("You are eaten by beasts, GAME OVER !!!")
        elif response3 == "yellow":
            print("YOU WIN YAYY !!!!!!!!!")
        else:
            print("GAME OVER !!!")
        