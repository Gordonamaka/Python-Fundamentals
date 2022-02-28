# A Sample Class - OOP Priniciples
# dir() command lists capabilities of performable operations - Never forget this.

# This is the template for making PartyAnimal objects
class PartyAnimal:
    x = 0
    # Each PartyAnimal object has a bit of data
    # Self: line 17
    def party(self):
      self.x = self.x + 1
      print("So far", self.x)

# Construct a PartyAnimal object and store in 'an'
an = PartyAnimal()
an.party()
an.party() # PartyAnimal.party(an)
an.party() # Self becomes an alias of an everytime it's called (invocation)
