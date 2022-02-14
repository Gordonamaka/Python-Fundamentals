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




