while True:
    print("Select the Arithmetic Operation")
    print("1.Addtion")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.I would like to stop and get the fuck out of here")
    choice = input("Enter the choice from 1 to 5 : ")
    if choice == "5":
        print("Thank u da mooditu po")
        break
    elif choice not in ('1','2','3','4','5'):
        print("Olungaana number type pannunga BRO")
        continue
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    if choice == "1":
        print("The answer is ", (a+b))
   
    elif choice == "2":
        print("The answer is ", (a-b))
   
    elif choice == "3":
        print("The answer is ", (a*b))
   
    elif choice == "4":
   
        if b==0:
            print("Aala vidu BRO")
        print("The answer is ", (a/b))

