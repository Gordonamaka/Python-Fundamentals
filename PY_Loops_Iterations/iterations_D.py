# Counting in a loop

# Example Set
numset = [9, 41, 12, 3, 74, 15]

# Counts how many lines ran.
def counting() :
  zork = 0 # count
  print('Before', zork)
  for num in numset :
    zork = zork + 1 
    print(zork, num)
  print('After', zork)

# Summing in a loop
def summing() :
  pork = 0 # count
  for sum in numset :
    pork = pork + sum
    print(pork, sum)
  print('After', pork)

# Finding the average in a loop
def average() :
  count = 0 #float(0) Automatically detects float variable in python3
  sum = 0 #float(0)
  print('Before', count, sum)
  for value in numset :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
  print('After', count, sum, sum / count)

# Filtering in a loop
def filter() :
  print('Before')
  for value in numset :
    if value > 20 :
      print('Large number', value)
  print('After')

# Search Using a boolean Variable
def search() :
  found = False
  print('Before', found)
  for value in numset :
    if value == 3 :
      found = True
    print(found, value)
  print('After', found)

# None type (how about that)
# Finding the smallest value
def findsmallest() :
  smallest = None # None means emptiness, nothing.
  print('Before')
  for value in numset :
    # line 67 for 'is' operator explanation
    if smallest is None :
      smallest = value
    elif value < smallest :
      smallest = value
    print(smallest, value)
  print('After', smallest)

# == means are they equal in type and value
# The "is" and "is not" Operations implies 'is (not) the same as' and is stronger than ==. 'is' seems to be strictly equal, whereas == is simply equal
# Try not to use 'is' or 'is not' too sparringly, mostly use it for 'None' or booleans.
