# Strings and lists are best friends.

# Split breaks a string into parts that produces a list of strings. We think of those as words. We can access a particular word or loop through all the words.
# Method exists in JS but this one is way easier.

abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

for w in stuff :
  print(w)

# When you do not specify a delimiter, multiple spaces are treated like one delimiter
line = 'A lot                      of spaces'
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split()
print(thing)

print(len(thing))

# You can specify what delimiter character to use in the splitting
thing = line.split(';')
print(thing)

print(len(thing))

fhand = open('mbox-short.txt')
for line in fhand:
  line = line.rstrip()
  if not line.startswith('From ') : continue
  words = line.split()
  print(words[2])

line = 'From alabama.countrymen.@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()

# The Double split pattern

# Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again

words = line.split()
email = words[1]
# Delimiter is '@'
pieces = email.split('@')
print(pieces[1]) # = uct.ac.za (Check)
# Much cleaner way