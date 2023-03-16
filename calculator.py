from functions import *

numbers = []
count = 1


while (True):
    print("Please enter numbers that you want to calculate.\n"
          "Press 'q' to quit the program"
          "Enter 'd' when you are done entering numbers.")
    while (True):
        number = input("Enter number {}: ".format(count))
        if number == 'd':
            count = 1
            break
        elif number == 'q':
            print("You have quitted the program.")
            exit()
        try:
            numbers.append(int(number))
        except ValueError:
            print("Please enter appropriate value!")
            continue
        count += 1

    print("1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n"
          "5. others")
    choice = input("Which function do you want to run?\n"
                   "Enter the number: ")

    if choice == '1':
        print(addition(numbers))
    elif choice == '2':
        print(subtraction(numbers))
