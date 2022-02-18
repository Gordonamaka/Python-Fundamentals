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
tmp = sorted(tmp, reverse=False) # True sorts in descending order, false or default is always ascending order. 
print(tmp)

# This is random, but you can reverse the reverse to have the list of tuples sorted by value but have the key first.
kmp = list()
for v,k in tmp:
  kmp.append( (k, v) )
print(kmp)

# Top 10 most common words in a file
def commonten(filename):
  
  fhand = open(filename) # Any file name or use input
  counts = dict()
  for line in fhand:
    words = line.split()
    for word in words:
      counts[word] = counts.get(word, 0 ) + 1
  
  lst = list()
  for key, val in counts.items() :
    newtup = (val, key) # flip to set up sort method by value.
    lst.append(newtup)
  
  lst = sorted(lst, reverse=True) # Desc order
  
  for val, key in lst[:10] : # Up to but not including 10 (0-9)
    print(key, val) # Wanted to print in key, val form b/c the list is already in descending order.

# Python can also handle in-line functionality (List comprehension)
print( sorted( [ (v,k) for k, v in d.items() ] ) )
# List comprehension [] creates a dynamic list. In this case, we make a list of reversed tuples and then sort it.