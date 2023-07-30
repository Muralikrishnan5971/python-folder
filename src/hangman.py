import random

life1 = """ 
  +-----+
    |   |
    o   |
        |
        |
        |
=========
     """

life2 = """ 
  +-----+
    |   |
    o   |
   /    |
        |
        |
=========
     """
life3 = """ 
  +-----+
    |   |
    o   |
   /|   |
        |
        |
=========
     """
life4 = """ 
  +-----+
    |   |
    o   |
   /|\  |
        |
        |
=========
     """
life5 = """ 
  +-----+
    |   |
    o   |
   /|\  |
   /    |
        |
=========
     """
life6 = """ 
  +-----+
    |   |
    o   |
   /|\  |
   / \  |
        |
=========
     """

print("Welcome to the Hangman game!!")

word_list = ["apple", "friend", "father", "orange", "honey"]
choosen_word = random.choice(word_list)
choosen_word_letters = list(choosen_word)

ans_word = []
blanks = len(choosen_word_letters)
for dash in range(0, blanks):
    ans_word.append("_")
print(" ".join(ans_word))

guess = input("please guess a letter ? ").lower()


life_counter = 1

# if guess in choosen_word_letters:
if guess in choosen_word_letters:
    print(f"The letter {guess} is present")
else:
    for i in range(0, 6):
        if life_counter == 1:
            print(f"You guessed {guess}, that's not in the word, You loose a life.")
            life_counter += life_counter
            print(life1)
        elif life_counter == 2:
            print(f"You guessed {guess}, that's not in the word, You loose a life.")
            life_counter += life_counter
            print(life2)
        elif life_counter == 3:
            print(f"You guessed {guess}, that's not in the word, You loose a life.")
            life_counter += life_counter
            print(life3)
        elif life_counter == 4:
            print(f"You guessed {guess}, that's not in the word, You loose a life.")
            life_counter += life_counter
            print(life4)
        elif life_counter == 5:
            print(f"You guessed {guess}, that's not in the word, You loose a life.")
            life_counter += life_counter
            print(life5)
        elif life_counter == 6:
            print(f"You guessed {guess}, that's not in the word, You loose a life. **YOU ARE DEAD**")
            life_counter += life_counter
            print(life6)
