# Matching and Extracting Data

# Re.search() returns a t/f depending whether or not the string matches
# If we actually want the matching strings to be extracted, we use re.findall()

import re
x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)

i = 'From: Using the : character'
j = re.findall('^F.+:', i)
print(j)

# Non greedy - Add the question mark
k = 'From: Using the : character'
l = re.findall('^F.+?:', k)
print(l)

# Fine-Turning String Extraction :
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst) # ['csev@umich.edu', 'cwen@iupui.edu']
