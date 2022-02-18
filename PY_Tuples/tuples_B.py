# Sorting a list of tuples
# We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary !

# First we sort the dictionary by the key using the items() method and sorted() function
d = {'a':10, 'b':1, 'c':22}
d.items() # Converts dictionary to a list of tuples. ('Set-like')

e = sorted(d.items()) # Sorted by the keys.
print(e)

# Using sorted() - Takes a sequence as a parameter and returns a sorted sequence
for k, v in e :
  print(k, v)

# What if you wanted to sort by values instead of key?
tmp = list()
for k,v in d.items() :
  tmp.append( (v, k) )
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

# This is random, but you can reverse the reverse to have the list of tuples sorted by value but have the key first.
kmp = list()
for v,k in tmp:
  kmp.append( (k, v) )
print(kmp)