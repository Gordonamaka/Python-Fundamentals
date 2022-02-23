# Writing a web browser using urllib

# Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file

import urllib.request, urllib.parse, urllib.error

# Open the URL url, which can be either a string or a Request object. Urlopen does the get request, encodes it, and receives all the headers. (Which we can access).
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand: # Run a loop for every line of the file
#   print(line.decode().strip())


# To make it like a file, we can store it in a dictionary

counts = dict()
for line in fhand:
  words = line.decode().split() # Need to decode because they're btyes not strings
  for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

# Reading Web Pages - Print the html.
# import urllib.request, urllib.parse, urllib.error
rpage = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in rpage:
  print(line.decode().strip())


