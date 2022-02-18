# Tuples are like lists - Another kind of sequence that functions much like a list

# Notice the round parentheses

x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

y = ( 1, 9, 2 )
print(y)

print(max(y))

for iter in y:
  print(iter)


# However, Tuples are "immutable" - once you create a tuple, you cannot alter its contents - similar to a string

# With tuples you cannot .sort(), .append(), .reverse(). Everything (I think) that you can do to modify a list, you cannot do to a tuple.

# On the other hand, Tuples are more efficient. They are simpler and more efficient in terms of memory use and performance than lists.

# When we are making "Temporary variables" we prefer tuples over lists.

# Tuples and Assignment - We can put a tuple on the left-hand side of an assignment statement. We can even omit the parentheses (Exclusive to Python).

(i,j) = (4, 'fred')
print(j)
(a, b) = (99, 98)
print(a)


# Tuples and Dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
  print(k,v)

tups = d.items()
print(tups)

# Tuples are comparable - Comparison operators work with tuples and other sequences. If the first item is equal, Python goes on to the end element, and so on, until it finds elements that differ.
(0, 1, 2) < (5, 1, 2) # True
(0, 1, 2000000000) < (0, 3, 4) # True
('Jones', 'Sally') < ('Jones', 'Sam') # True
('Jones', 'Sally') > ('Adams', 'Sam') # True

