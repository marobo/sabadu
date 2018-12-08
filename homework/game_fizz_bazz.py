import timeit
def fb_game():
    number = range(100)
    for fb in number:
        if fb % 5 == 0 and fb % 3 == 0:
            print("Fizz Buzz")
        elif fb % 3 == 0:
            print("Fizz")
        elif fb % 5 == 0:
            print("Buzz")
        else:
            print(fb)
print (fb_game())
