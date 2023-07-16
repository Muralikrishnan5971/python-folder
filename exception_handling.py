
# items_in_cart = 0
# assert(items_in_cart == 2)

# if items_in_cart != 2:
#      raise Exception("Items in Cart is not equal to 2")

try:
   with open('fewEFWF.txt') as f:
     f.read()

except:
   print("I am printing because the given file does does not exist")


try:
   with open('fsdsdfdsaw.txt') as f:
      f.read()

except Exception as e:
   print(e)

finally:
   print("cleaning up resources done...")