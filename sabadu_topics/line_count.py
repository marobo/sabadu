def line_count():
    import os, os.path
    while True:
        file_location=eval(input("Which file do you want ot open?"))
        
        if os.path.isfile(file_location) and os.access(file_location, os.R_OK):
            print("Ok")
            break
        else:
            print("This not a file") 
    print((file_location + "is a valid file"))
    line_count = 0
    emtpy_line_count = 0
    long_count = 0
    with open(file_location) as f:
        for line in f:
            line_count += 1
            if line == '\n':
                emtpy_line_count += 1
            if len(line) > 20:
                long_count += 1
 
    print((line_count, emtpy_line_count, long_count))
line_count()
