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