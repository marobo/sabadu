__author__ = 'ony'


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def raisePower(x, y):
    return x ** y


def myCalculator():
    try:
        choice = input("Operation to perform: \n( + ) Addition \n( - ) Subtraction \n( * ) Multiplication \n( / ) Division \n( n* ) Raising a power to number \n Enter choice: ")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '+':
            print(num1, "+", num2, "=", addition(num1, num2))
            print(" ")
            print("-------------------------------")
            myCalculator()

        elif choice == '2':
            print(num1, "-", num2, "=", subtraction(num1, num2))
            print(" ")
            print("-------------------------------")
            myCalculator()

        elif choice == '3':
            print(num1, "*", num2, "=", multiplication(num1, num2))
            print(" ")
            print("-------------------------------")
            myCalculator()

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))
            print(" ")
            print("-------------------------------")
            myCalculator()

        elif choice == 'n*':
            print(num1, "**", num2, "=", raisePower(num1, num2))
            print(" ")
            print("-------------------------------")
            myCalculator()

        else:
            print("You have not typed a valid operator, please run the program again.")

    except ValueError:
            print("Invalid Value")

myCalculator()
