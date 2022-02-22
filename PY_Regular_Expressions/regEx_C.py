# RegEx - Practical Applications
# We can use Regex to parse strings and other data.

import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', lin) 
"""
The [^ ] is to specify a matching schema to match non-blank characters and the * is to signify that we want to match many of them. 
We can make this more specific by adding '^From .*@([^ ]*' which starts at the begginning of the line, to look for the string 'From'.
"""
print(y)

# We can also look for this to find lines in a file which we've done previous with the mbox.short.txt exercise

hand = open('mbox-short.txt')
numlist = list() # Create a list
for line in hand: # For each line in the indicated file
  line = line.rstrip() # Remove whitespaces to the right
  stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line) # Find all that exists with the given parameters for each line
  if len(stuff) != 1 : continue # if one instance does not exist with the line X-DSPAM-Confidence: (using length as an indicator) continue on and repeat the iteration. (Skip all the lines that don't match, fall through when it does.)
  num = float(stuff[0]) # Transform into a float variable
  numlist.append(num) # Add it to the list on line 16
(print('Maximum:', max(numlist))) # Return the biggest item in said list. 0.9907


# Escape Character - If you want a special regular expression character to just behave normally (most of the time) you prefix it with '\'
i = 'We just received $10.00 for cookies.'
k = re.findall('\$[0-9.]+', i) # Non-greedy regex would stop at $1, but we use greedy to get everything after that
# \$ indicates a real dollar sign, 0-9. indicates a digit or period, and + indicates at least one or more (aka the greedy factor, +? would be non-greedy).
print(k)