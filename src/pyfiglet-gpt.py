# import pyfiglet
# import time
# import os

# def clear_screen():
#     # Function to clear the console screen
#     os.system('cls' if os.name == 'nt' else 'clear')

# def display_ascii_art(text):
#     # Function to display ASCII art
#     font = pyfiglet.Figlet()
#     ascii_art = font.renderText(text)
#     print(ascii_art)

# def welcome_animation(text, delay=0.5, iterations=5):
#     # Function to create a simple animation
#     for _ in range(iterations):
#         clear_screen()
#         display_ascii_art(text)
#         time.sleep(delay)

# if __name__ == "__main__":
#     welcome_text = "Welcome to Youtube Channel"
#     welcome_animation(welcome_text)

import pyfiglet
import time
import os

def clear_screen():
    # Function to clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def display_fish():
    # Function to display ASCII art of a fish
    font = pyfiglet.Figlet()
    fish_art = font.renderText('><((("> ')
    return fish_art

def swim_animation(width=40, duration=10, delay=0.1):
    # Function to create a fish swimming animation
    clear_screen()
    frames = width - 10
    for _ in range(duration):
        for i in range(frames):
            clear_screen()
            print(' ' * i + display_fish(), end='', flush=True)
            time.sleep(delay)
        for i in range(frames, 0, -1):
            clear_screen()
            print(' ' * i + display_fish(), end='', flush=True)
            time.sleep(delay)

if __name__ == "__main__":
    swim_animation()
