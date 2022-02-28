# Inheritence - The ability to create a new class by extending an existing class. (Sub-classes)

# Subclasses are more specialized versions of a class, which inherit attributes and behaviours from their parent classes and can introduce their own.

class PartyAnimal:
  # These are class attributes - A variable within a class
  x = 0
  name = "" 

  # These are class methods - A function within a class
  def __init__(self, nam):
    self.name = nam
    print( self.name ,'constructed' )
  
  def party(self):
    self.x = self.x + 1
    print(self.name, "party count", self.x)


# FootballFan is a class which extends PartyAnimal. It has the capabilits of PartyAnimal and more.
class FootballFan(PartyAnimal):
  points = 0
  
  def touchdown(self):
    self.points = self.points + 7
    self.party()
    print(self.name, 'points', self.points)

# An object is a particular instance of a class
# The PartyAnimal constructor is code that runs when an object is created
s = PartyAnimal("Sally")
s.party()

# This extends the class to make a new class (FootballFan)
j = FootballFan("Jim")
j.party()
j.touchdown()


"""
Summary
OOP is a very structured approach to code reuse
We can group data and functionality together and create many independent instances of a class
"""