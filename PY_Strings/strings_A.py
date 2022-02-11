# We can get any single character in a string using an index specified in square brackets
fruit = 'banana'
letter = fruit[1]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

# Len gives us back the length of a str
l = len(fruit)
print(l)

# Looping through strings
def throstr() :
  index = 0
  while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index + 1 # Count pattern.

def prefer() : # We prefer for loops
  for letter in fruit:
    print(letter)

def countfruit():
  word = 'banana'
  count = 0
  for letter in word :
    if letter == 'a' :
      count = count + 1 # Counts the amount of 'a''s
  print(count)

