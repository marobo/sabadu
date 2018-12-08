- What does chmod +x  <filename> do?
    chmod +x <filename> is a command to grant the excution permission to a file
- Why do you need `#!/usr/bin/env python` on the first line of runme.py?
    UNIX doesn't know to use python on .py files.
    So we tell UNIX to use /usr/bin/env python to execute the file.
- What is `$PATH`?
    $PATH is an environmental variable.
    $PATH lists directories which contain binaries (e.g. /usr/local/bin)
- Why does `$PATH` begin with a `$`?
    In BASH and other languages, all variables must begin with `$`
- What is a symbolic link?
    A symbolic link is a reference to a file on the file system
- Why would you use a symbolic link?
    1) You may want to reference a single file by different names
    2) You may want to reference a single file in different locations
- How do you create a symbolic link?
    1) Find the full path to file you want to link to
    2) Find the full path to the directory you want to put the symbolic link
    3) You run the command 
        ln -s <path_of_file> <path_of_directory>
  

chmod XXX filename
==================

o + x
u - w
g + r
user/group/other +/- read/write/execute

ugo = user/group/other
r = read
w = write
x = execute

 u  g  o
rwxrwxrwx
111111111

ugo:
777

1 = execute
2 = write
3 = execute + write = 1 + 2
4 = read
5 =	execute + read = 4 + 1
6 = write + read = 2 + 4
7 = execute + write + read = 1 + 2 +4


Exemple:
========
In command:
$ chmod 777 README.md
$ ls -al
drwxrwxr-x 2 ony ony   4096 Jun 17 10:00 .
drwxrwxr-x 4 ony ony   4096 Jun 16 00:15 ..
-rwxrwxrwx 1 ony ony    255 Jun 10 00:32 README.md


# Instructions for making a python file executable

Make a python file `ask.py`
Write a python print statement in the file
run the file with `python ask.py`

Try to run with just `./ask.py`
You see permission denied!
Check the file permissions with `ls -l ask.py`

Change the file permissions with `chmod +x ask.py`
Check the file permissions with `ls -l ask.py`
Notice the x, this means the file executable now

Try running `./ask.py`
Notice the syntax error, because this computer doe not know to use python!

Add a shebang at the top of the file `#!/usr/bin/env python`
Try to run with just `./ask.py`
See python print!

# Adding a command to your virtual environment

1. run `echo #PATH`, run `deactivate`, run `echo $PATH` again, and notice the difference. The path inside your environment has one more directory to search for commands

2. create a symbolic link inside this new directory to you ask.py file
  - find the full path of the new $PATH directory - this is the first entry in `echo $PATH`
  - find the full path to your ask.py file, for me this is `/users/petercoward/Devel/script/ask.py`
  - create your symbolic link `ln -s /users/petercoward/Devel/script/ask.py <your venv path bin dir>`

