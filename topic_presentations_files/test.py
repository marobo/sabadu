from operator import add, sub, mul, truediv, pow


choice = input("Operation to perform: \n( + ) Addition \n( - ) Subtraction \n( * ) Multiplication \n( / ) Division \n( ^ ) Raising a power to number \n Enter choice: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '^': pow,
}

print(operators[choice](num1, num2))
