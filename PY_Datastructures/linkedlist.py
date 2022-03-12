# Linked List Example

class Node:
  def __init__(self, data=None, next=None):
      self.data = data
      self.next = next # Pointer


class LinkedList:
  def __init__(self):
      self.head = None # Points to head.

  # Insert At Beginning (head)
  def insert_at_beginning(self, data):
      node = Node(data, self.head) # Instance of Node class
      self.head = node
      

  # Insert At End
  def insert_at_end(self, data):
    if self.head is None:
        self.head = Node(data, None) # The next of the end=null (none)
        return
    
    itr = self.head
    while itr.next:
        itr = itr.next
    
    # When  reaches null, then you're at the last element.
    itr.next = Node(data, None)
  
  
  # Insert At End
  def insert_values(self, data_list): # data_list to create a new list
    self.head = None # Clears current list
    for data in data_list:
        self.insert_at_end(data) # using beginning would reverse
  
  
  # Remove an Element
  def remove_at(self, index):
    if index < 0 or index >=  self.get_length():
        raise Exception('Invalid Index')
    
    if index==0: # Moves to the next pointer
        self.head = self.head.next
        return
    
    count = 0 # You have to manually maintain the count
    itr = self.head
    while itr:
        if count == index - 1: # You want to modify the next pointer of the previous element (IMPORTANT)
          itr.next = itr.next.next
          break
        
        itr = itr.next
        count += 1 # Don't forget to maintain the counter
  
  
  # Insert an Element
  def insert_at(self, index, data):
    if index < 0 or index > self.get_length():
        raise Exception("Invalid Index")
    
    if index==0:
        self.insert_at_beginning(data)
        return
    
    count = 0 # Other than the first index, you need to maintain count
    itr = self.head
    while itr:
      if count == index - 1: # You want to modify the next pointer of the previous element (IMPORTANT)
        node = Node(data, itr.next) # Previous elements next would be this element.
        itr.next = node
        break
      
      itr = itr.next # Going thru the ll
      count += 1
  
  # Print the ll
  def print(self):
      if self.head is None: # If it's blank
          print("Linked List is Empty")
          return

      # Iterator variable
      itr = self.head
      llstr = ''
      
      while itr:
          llstr += str(itr.data) + '--->'
          itr = itr.next
      
      print(llstr)
  
  # Print the ll length
  def get_length(self):
    count = 0 # Counter
    itr = self.head # Beginning
    while itr:
      count+=1 # Incrementor
      itr = itr.next # Keep moving next until none.

    return count

""" 
                            PRACTICE 
1. insert after value (not index) 
insert_after_value(self, data_after, data_to_insert):

- Search for first occurance of data_after value in linked list
- Now insert data_to_insert after data_after node.

2. remove by value (not index)
def remove_by_value(self, data):

- Remove first node that contains data argument.

3A. Implemement a doubly linked List. (In a new file)
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

B) Add new methods
i) def print_forward(self):

- This method prints list in forward direction. Use node.next

ii) def print_backward(self):

- Print Linked List in reverse direction. Use node.prev for this.

iii) Implement all other methods in regular linked list class and make necessary changes for doubly linked list(you need to populate node.prev in all those methods.)

"""


if __name__ == '__main__':
  ll = LinkedList()
  ll.insert_at_beginning(2)
  ll.insert_at_beginning(1)
  ll.insert_at_end(5)
  # ll.insert_values(['banana', 'mango', 'metal gear solid 4'])
  # ll.remove_at(2)
  ll.insert_at(2, 3)
  ll.insert_at(3, 4)
  ll.insert_at(5, 'Calling all Spider Riders') # This indicates that the last none/null value in the linked list exists and holds a none value. Which would allow you to insert at the end of the ll.
  
  
  print('Length:', ll.get_length())
  
  
  ll.print()


