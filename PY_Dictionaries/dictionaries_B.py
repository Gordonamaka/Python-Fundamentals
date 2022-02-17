# One of the common use of dictionaries is counting how often we 'see' something

# We can use the in operator to see if a key is in the dictionary
# ccc = dict()
# 'csev' in ccc

# Dictionary iterators - Making a histogram
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

def counter():
  for name in names :
    if name not in counts :
      counts[name] = 1
    else :
      counts[name] = counts[name] + 1
  return counts
# print(counts) returns *None* when used in a function


# Simplified count with get() - We can use it to provide a default value of zero when the key is not yet in the dict - and then just add one
for name in names :
  counts[name] = counts.get(name, 0) + 1
print(counts)


# The get method for dictionaries - The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common that there is a method called get() that does this for us. (Doesn't exist in JS)
if name in counts:
  x = counts[name]
else :
  x = 0 # default

# This line is equivalent to 23 - 26, but in one line.
x = counts.get(name, 0) # (key, default), if the key doesn't exist you get the default, if it does, you get what was inside the key.

