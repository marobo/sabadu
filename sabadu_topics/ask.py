#!/usr/bin/env python

name = input("Enter your name: ")
ages = int(input("Enter your ages: "))

print(("Hello {}, you have {} years old").format(name, ages))

if ages < 50:
    print ("You are very young")
else:
    print ("you are about to die")
