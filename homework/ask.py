#!/usr/bin/env python

name = raw_input("Enter your name: ")
ages = int(raw_input("Enter your ages: "))

print ("Hello {}, you have {} years old").format(name, ages)

if ages < 50:
    print ("You are very young")
else:
    print ("you are about to die")
