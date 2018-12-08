# Homework - add the file depth to the print statement
import os

# Write that list of files to `manifest.txt` in that directory (edited)
with open('manifest.txt', 'w') as manifest:

    # Read all the files that are in a directory
    for file_name in os.listdir('.'):
        manifest.write(file_name + '\n')
        if os.path.isdir(file_name):
            print(('|'), (file_name))
        elif os.path.isfile(file_name):
            print(('|____'), (file_name))
        else:
            print(('---'), (file_name))
