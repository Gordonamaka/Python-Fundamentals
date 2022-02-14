# File handle as a sequence

# A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence 

# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
  # count = count + 1
# print('Line count:', count)

# A sequence is an ordered set and we can iterate through it via a for-loop

# Reading the whole file: Method - .read()
# inp = fhand.read()
# print(inp[:20]) - first 20 characters, beginning & up to/not including 20.

# Searching thru a file...
# for line in fhand:
  # if line.startswith('From:') :
    # Print(line)
# The for loop doesnt throw the \n new lines away
# New line is considered white space and can be stripped using rstrip().

# Skipping with continue...
# for line in fhand:
  # line = line.rstrip()
  # if not line.startswith('From: ') :
    # continue
  # print(line)
# We can conveniently skip a line/iteration by using the continue statement

# Using in to select lines
# We can look for a string anywhere in a line as our selection criteria 
# for line in fhand:
  # line = line.rstrip()
  # if not 'selection criteria' in line :
    # contine
  # print(line)

# Filename can also be inputted as an input prompt
# for bad file names, or files that do not exist, you can include try/except(quit()) for insurance. Without quit it would continue. This allows the entire python program to end without a traceback.  




