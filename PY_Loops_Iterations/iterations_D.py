# Counting in a loop
numset = [9, 41, 12, 3, 74, 15]

def counting() :
  zork = 0 # count
  print('Before', zork)
  for num in numset :
    zork = zork + 1 # Counts how many lines ran.
    print(zork, num)
  print('After', zork)

def summing() :
  # Summing in a loop
  pork = 0 # count
  for sum in numset :
    pork = pork + sum
    print(pork, sum)
  print('After', pork)

def average() :
  # Finding the average in a loop
  count = float(0)
  sum = float(0)
  print('Before', count, sum)
  for value in numset :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
  print('After', count, sum, sum / count)

print(average())