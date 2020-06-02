"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

import os


def read_and_print(file_name):
    f = open(file_name, "r")
    data = f.read()
    print(data)
    f.close()

read_and_print("c:/Users/Rose/Desktop/Git/Lambda/06-CS/01-Intro-to-Python-and-OOP/Intro-Python-I/src/foo.txt")

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

def create_and_print(file_name):
    f = open(file_name, "w")
    f.write("arbitrary content\narbitrary content\narbitrary content")
    f.close()
    r = open(file_name, "r")
    data = r.read()
    print(data)
    r.close()

create_and_print("bar.txt")