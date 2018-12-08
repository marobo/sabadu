from operator import add, sub, mul, truediv, pow

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '^': pow,
}


def myCalculator():
    while True:
        try:
            choice = input("Operation to perform: ")
            if choice in operators:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(operators[choice](num1, num2))
            else:
                print("Operation perform you entered is not valid, please run it again")
                break 

        except ValueError:
                print("Value is not valid")

myCalculator()
