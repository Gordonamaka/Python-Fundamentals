# Object life cycle

"""
Objects are created, used and discarded
We have special blocks of code (methods) that get called
  - At the moment of creation (constructor)
  - At the moment of destruction (destructor)
Constructors are used a lot
Destructors are seldom used

In OOP, a constructor in a class is a special block of statements called when an object is created.
"""

class PartyAnimal:
  x = 0
  
  # Constructor - Usually used to set up variables
  def __init__(self):
    print('I am constructed')
  
  def party(self):
    self.x = self.x + 1
    print('So far', self.x)
  
  # Destructor
  def __del__(self):
    print('I am destructed', self.x)


an = PartyAnimal()
an.party()
an.party()
# After this step, the destructor is called. 'Destroying' the object. Now it is no longer an object, it is an integer variable.
an = 42
print('an contains', an)


"""
Constructors can have additional parameters. These can be used to set up instance variables for the particular instance of the class (i.e., for the particular object)
"""
class PartyAnimal:
  x = 0
  # Empty name that is inputed to the z parameter (line 46-47, 54)
  name = "" 

  def __init__(self, z):
    self.name = z
    print( self.name ,'constructed' )
  
  def party(self):
    self.x = self.x + 1
    print(self.name, "party count", self.x)


# We can create two independent instances
s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()