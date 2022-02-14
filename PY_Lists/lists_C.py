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
