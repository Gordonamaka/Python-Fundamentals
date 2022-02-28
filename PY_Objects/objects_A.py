# Quick details about data structures

"""
list.append(x)
  - Add an item to the end of the list, same as a[len(a):] = [x]
list.extend(l)
  - Extend the list by appending all items in the given list, same as a[len(a):] = L
list.insert(i,x)
  - Insert an item at a given position. The first arguement is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is the same as a.append(x)
list.remove(x)
  - Remove the first item from the list whose value is x. It is an error if there is no such item.
list.pop([i])
  - Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
  
  https://docs.python.org/3/tutorial/datastructures.html
"""

# An object is a bit of self-contained code and data, a key aspect of which is to break the problem into smaller understandable parts (divide and conquer)

"""
Definitions:

Class - a template - Dog

Method or Message - A defined capability of a class - bark()

Feild or attribute - A bit of data in a class - length

Object or Instance - A particular instance of a class - Lassie.
"""
