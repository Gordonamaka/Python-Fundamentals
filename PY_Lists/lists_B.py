# You can concatenate existing lists using '+' and create an entirely new list

a = [ 1, 2, 3 ]
b = [ 4, 5, 6 ]
c = a + b
print(c)

# Lists can be sliced using :
# Just like with strings, the second number is 'up to but not including'
t = [ 9, 41, 12, 3, 74, 15 ]
t[ 1:3 ] # = [ 41, 12 ]
t[ :4 ] # = [ 9, 41, 12, 3 ]
t[ 3: ] # = [ 3, 74, 15 ]
t[ : ] # = entire list.

# List methods
x = list()
type(x)
# dir(x) for all the built in list methods.

# We can create an empty list and then add things to that list using the append method. The list stays in order and new elements are added at the end of the list. (Much like the .push method in javascript)
stuff = list() # We can also just used empty square brackets []
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print('stuff')

# Is something in a list? (Same thing as .includes in Javascript)
some = [ 1, 9, 21, 10, 16 ]
9 in some # True
15 in some # False
20 not in some # True

# Lists are in order
t.sort()
print(t)
# Weirdly enough, setting the sort as it's own variable returns 'none'
# Ex:) st = t.sort() \n print(st)

# List methods used often
print(len(t)) # Prints length
print(max(t)) # Finds and prints Max num
print(min(t)) # Opposite of max, finds & prints min
print(sum(t)) # sum of all the list elements
print(sum(t)/len(t)) # Prints the average


# Two code bases that do the same thing but simplified with Lists

# Without lists - Uses less memory
total = 0
count = 0
while True :
  inp = input('Enter a number: ')
  if inp == 'done' : break #inline functionality in python?
  value = float(inp)
  total = total + value
  count = count + 1
average1 = total / count
print('Average', average1)

# With lists - BUT It uses more memory...
numlist = list()
while True:
  inp = input('Enter a number: ')
  if inp == 'done' : break #inline functionality in python?
  value = float(inp)
  numlist.append(value)
average2 = sum(numlist) / len(numlist)
print('Average:', average2)

