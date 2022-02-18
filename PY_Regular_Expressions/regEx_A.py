# Understanding Regular Expressions

"""
Regular Expression Quick Guide

^       Matches the beginning of a line
$       Matches the end of the line
.       Matches any character
\s      Matches Whitespace
\S      Matches any non-whitespace character
*       Repeats a character zero or more times
*?      Repeats a character zero or more times (non-greedy)
+       Repeats a character one or more times
+?      Repeats a character one or more times (non-greedy)
[aeiou] Matches a single character in the listed set
[^XYZ]  Matches a single character not in the listed set
[a-z0-9]The set of characters can include a range
(       Indicates where string extraction is to start
)       Indicates where string extraction is to end.

"""

# Before using Regex you must import 'import re'

# You can use re.search() to see if a string matches regex, and re.findall() to extract portions of a string that match your regex.