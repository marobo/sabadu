def start_pattern():
    print("Program to print start pattern: \n")
    rows = int(input("Enter max star to be display on single line: "))
    for i in range(0, rows):
            print("*", end=' ')
        print("\r")

    for i in range(rows, 0, -1):
            print("*", end=' ')
        print("\r")


start_pattern()
