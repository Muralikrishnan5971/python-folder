import os

for root, dirs, files in os.walk('.'):
    #print("ROOT -->", root)
    #print("Sub Directory List -->", dirs)
    print("File List -->", files)



