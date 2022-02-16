# Slicing Strings
# We can look at any continuous section of a string using a colon operation :
s = 'Monty Python'
print(s[0:4])
# The second number is one beyond the end of the slice - 'up to but not including'
print(s[6:7])
# No traceback, it'll go to the end
# Hence,if the second number is beyond the end of the string, it stops at the end.
print(s[6:20])


# If we leave off the first number or the last number of the slice, it is assumed to be the beginning or end of the string respectively.
print(s[:2]) # up to but not including two.
print(s[8:]) # 8 through to the end.
print(s[:]) # Entire string, but unnecessary.

# Using in as a logical operator
# The in keyword can be used to check to see if one string is "in" another string
fruit = 'banana'
'n' in fruit # T
'm' in fruit # F
'nan' in fruit # T
if 'a' in fruit :
# The in expression is a logical expression that returns True or False and can be used in an if statement
  print('Found it!')

# String Comparison, case can make this up, could be hard to predict.
# if word == 'banana' :
#   print('All right, bananas.')

# if word < 'banana' :
#   print('Your word,' + word + ', comes before banana.')
# elif word > 'banana' :
#   print('Your word,' + word + ', comes after banana.')
# else:
#   print('All right, bananas.')


# Strings are objects and therefore have methods. (String library). Rmr they don't modify the original string.
greet = 'Hello Bob'
zap = greet.lower()
print(zap) # Lower case
cap = greet.upper()
print(cap) # Upper case

# dir() is a powerful inbuilt function in Python3, which returns list of the attributes and methods of any object (say functions , modules, strings, lists, dictionaries etc.)
dir(greet)

# Searching a string - We can use the find() function to search for a substring within another string (The first occurrence, returns -1 if nothing is found.)
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)

# Search and Replace - replace() replaces all occurrences of the search string with the replacement string **REPLACE() IS CASE SENSITIVE**
moveit = greet.replace('Bob', 'Jane')
print(moveit)
moveon = greet.replace('o', 'x')
print(moveon)

# Stripping Whitespace - lstrip() and rstrip() remove whitespace at the left or right
# strip() removes both beginning and ending whitespace.

# Prefixes
line = 'Please have a nice day'
line.startswith('Please') # True
line.startswith('P') # False


# Parsing and Extracting
data = 'From alabama.countrymen.@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos) # Space is the value point, indicating that it will find the first instance, FROM atpos, which is the start point. Default is zero.
# A third argument is available (end) to indicate where to end the search. Default is the end of the string.
print(sppos)

host = data[atpos+1 : sppos] # Index position after 21 = atpos + 1
print(host)