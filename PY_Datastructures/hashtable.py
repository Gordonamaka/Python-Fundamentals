# Hash Table Example

""" hash function Example
def get_hash(key):
  h = 0
  for char in key:
    # ord to get the unicode code point for a one-character string
    h += ord(char)
  return h % 100
"""

class HashTable:
  def __init__(self):
      self.MAX = 10 # Table total
      self.arr = [[] for i in range(self.MAX)] # initializing size 100 arr, the default value for each is [].
    
  def get_hash(self, key):
      h = 0
      for char in key:
        h += ord(char)
      return h % self.MAX
  
  def __setitem__(self, key, val):
      # Simply getting the hash of the key
      h = self.get_hash(key)
      found = False
      # Find out if it exists to avoid collisions
      for idx, element in enumerate(self.arr[h]): # Enumerate provides a counter while looping through this single hash idx (maintaining the count is necessary).
          if len(element) == 2 and element[0]==key: # if the element length has 2 elements (a key,val pair) & the first element (the key) already exists with the key given
            self.arr[h][idx] = (key,val) # Now the hash of that index location will store a linked list of both key value pairs.
            found = True
            break
      if not found:
          self.arr[h].append((key,val))
      
      # Setting the value at the index of the ll
    
  # Get value given the key.
  def __getitem__(self, key):
      h = self.get_hash(key)
      for element in self.arr[h]: # loop thru list
          if element [0] == key:
              return element[1] # if it matches return the second element (value)
  
  def __delitem__(self,key):
    h = self.get_hash(key)
    for index, element in enumerate(self.arr[h]): # first find the index, then go thru the elements, and when you find a particular element, then you want to delete
        if element[0] == key:
          del self.arr[h][index]

""" Python has a set/get item operators to make it easier 
  # Adding a key value pair to your hash
  def set(self, key, val):
      # Simply getting the hash of the key
      h = self.get_hash(key)
      self.arr[h] = val # Setting the value at the index of the hash
  
  def get(self, key):
      h = self.get_hash(key)
      return self.arr[h]
"""

t = HashTable()
# t["march 1"] = 20
# t["march 6"] = 120
t["march 6"] = 78
t["march 8"] = 67
t["march 9"] = 4
t["march 17"] = 459
del t['march 6']
del t['march 17']
# print(t['march 6'])
print(t.arr)