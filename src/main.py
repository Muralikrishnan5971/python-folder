def repeat(text, repetition):
    return f"{text}\n" * repetition

def main():
      print("this is a main function")
      
# text = input("Enter some text: ")
# print(repeat(text, 5))

"""
Now when we try to execute the above script, using python, it works
When tried from python interpreter as show below

>>> from main import repeat

the script get executed automatically. 
i.e, Even if we are just importing a function, the whole file gets executed first,
and then the definitions are imported in.

similarly if we import the same function into another .py file and exectute it,
main.py gets exectued first, which we dont want.

here comes, if __name__ == '__main__':

How it works ?

When we run python main.py, python sets the __name__ dunder variable to __main__
Then in the if condition we check for the same.

"""
if __name__ == '__main__':
	text = input("Enter some text: ")
	print(repeat(text, 5))
	main()