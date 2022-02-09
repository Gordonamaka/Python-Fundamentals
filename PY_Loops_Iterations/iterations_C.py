# Loop idioms: What we do in Loops

# Making smart loops
# The trick is "knowing" something about the whole loop when you are stuck writing code that only sees one entry at a time.

# Looping thru a set
print('Before')
numset = [9, 41, 12, 3, 74, 15]
for num in numset :
  print(num)
print('After')

# Can we sort this intuitvely
for num in numset :
  if num > 45 :
    print("Greater")
  else :
    print('Lower')
# Not exactly

# Finding the largest value
largest_so_far = -1
print('Before', largest_so_far)
numset = [9, 41, 12, 3, 74, 15]
for the_num in numset :
  if the_num > largest_so_far :
    largest_so_far = the_num
  print(largest_so_far, the_num)
# The number is set & stored in the variable on line 21.
print('After', largest_so_far)
