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
  count = float(0)
  sum = float(0)
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


