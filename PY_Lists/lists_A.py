# Algorithm - A set of rules or steps used to solve a problem
# Datastructures - A particular way of organizing data in a computer.

# A list is a kind of collection
# A collection allows us to put many values in a single 'variable'
# A collection is nice because we can carry all many values around in one convenient package

friends = [ 'Joseph', 'Glenn', 'Sally' ]

carryon = [ 'socks', 'shirts', 'perfumes' ]

# List constants are surrounded by square brackets and the elements in the list are separated by commas (similar to arrays but not to be confused for arrays.)
# A list element can be any python object - even another list [ 1, 4, [ 5, 6 ], 8 ]
# A list can be empty []

# Lists are mutable but strings are immutable
# We can check the length (len(list))

# The range() function
print(range(4))
print(len(friends))
print(range(len(friends)))
# The range function returns a list of numbers that range from zero to one less than the parameter
# We can construct an index loop using for and an integer iterator.

for i in range(len(friends)) :
  friend = friends[i]
  print('Happy Birthday:', friend)