# A list is a linear collection of values that stay in order. (Order Matters)
# Whereas a dictionary is a 'bag' of values, each with its own label. (Key and a value)

# Dictionaries are objects in Python
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 75
print(purse)

# We index the things we put in the dictionary with a 'lookup tag'
print(purse['candy'])

purse['candy'] = purse['candy'] + 2
print(purse)

# Pythons dictionaries can not use dot notation like in Javascript, only bracket notation [].


# Comparing Lists and Dictionaries
# Dicts use keys instead of numbers to look up values

# List
lst = list()
lst.append(21)
lst.append(183)
print(lst)
[21, 183]
lst[0] = 23
print(lst)

# Dict
ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)

# Dictionary Literals (Constants) - A list of key : value pairs.
# You could make an empty dictionary using empty curly braces. 
jjj = { 'chuck' : 1, 'fred' : 42, 'jan': 100 }
print(jjj)
ooo = {  }
print(ooo)
