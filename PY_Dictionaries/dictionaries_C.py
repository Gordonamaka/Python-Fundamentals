# Counting Pattern in Dicts
# The general pattern is to split the line into words, then loop through the words and use a dictionary to track the count of each word independently

counts = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
  counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

# Retrieving lists of keys and values from a dictionary
jjj = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# 1. list()
print(list(jjj))
# 2. keys()
print(jjj.keys())
# 3. Values() - Had to predict the order under certain circumstances.
print(jjj.values())
# 4. items() - Which is a Tuple.
print(jjj.items())

# Two iteration variables !! We can loop through the key-value pairs in a dictionary using *two* iteration variables

for aaa,bbb in jjj.items() :
  print(aaa, bbb)

# Each iteration, the first variable is the key and the second variable is the corresponding value for the key.

# Python is the only language I know with two iteration variables ! (Cool Stuff)


# Intersecting Files and dictionaries
name = input('Enter file: ')
handle = open(name)

counts = dict()
# Iteration that goes through each line in the file
for pline in handle :
  # Splits them into an array
  words = pline.split()
  # Make a histogram for the count
  for word in words:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
# Loop thru the key value pairs
for word,count in counts.items() :
  if bigcount is None or count > bigcount :
    bigword = word
    bigcount = count

print(bigword, bigcount)