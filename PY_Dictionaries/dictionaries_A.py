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