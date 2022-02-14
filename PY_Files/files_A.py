# Using open()

handle = open(filename, mode)
# Returns a handle use to manipulate the file

# Filename is a string

# Mode is optional and should be 'r' if we are planning to read the file and 'w' if we are going to write to the file.

# fhand = open('mbox.txt', 'r') for example, albeit, if the file doesn't exist, you'll get a traceback

# New line: \n