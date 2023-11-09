import random
import os
import time

def print_ascii(fn):
    f= open(fn,'r')
    print(''.join([line for line in f]))
    time.sleep(0.10)

art = ['007.txt', 'shark.txt', 'monkey.txt', 'gitlogo.txt', 'kiki.txt', 'batmanlogo.txt', 'satellite.txt', 'kiss.txt', 'keyboard.txt']

for i in range(1, 125):
    
    print_ascii(random.choice(art))
    os.system('clear')

