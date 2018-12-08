#marks4.py
# program averages a set of student marks input by the user.
# user inputs a sentinel value (-1) at the prompt to signal they want to stop
# written by P.K., January 24 2005

print "You will be prompted to input the marks one at a time."
print "You should signal when you wish to stop by inputting -1 at the prompt \n"

total = 0.0    # Ensures that total is a float so float division is performed
count = 0   # counts the number of marks input
mark = input("Enter mark (or -1 to stop): ")

while mark != -1:
    total = total + mark
    count = count + 1
    mark = input("Enter mark (or -1 to stop): ")

if count == 0:
    print "Goodbye"
else:
    average = total / count
    print "\nThe average mark (to 1 dp) is %0.1f" % average