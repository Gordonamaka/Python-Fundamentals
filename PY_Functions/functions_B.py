# We create a new function using the def keyword followed by optional parameters in parentheses
# We indent the body of a function to storage instructions in memory.
def greet(lang): #stands for language argument, depending on what's inputting will change the argument output (function invocation).
  if lang == 'es':
    return 'Hola'
  elif lang == 'fr':
    return 'Bonjour'
  else:
    return 'Hello'

print(greet('es'), "senorita")
# greet('en')
# greet('es')
# greet('fr')
# greet('turkey bacon') 
# The else statement merely prints Hello whether we've given it an english argument or not.

# Return values in functions: Often a function will take its arguments, do some computation, and return a value to be used as the value of the function call in the calling expression. The return keyword is used for this.

def sup():
  return "Hello"

print(sup(), "Mobi")
print(sup(), "Jello Bello")

# Multiple Parameters / Arguments
def addtwo(a , b):
  added = a + b
  return added

x = addtwo(5, 5)
print(x)

# Functions that return values are "fruitful functions"

# Void functions are 'Not fruitful', hence they do not return values.

# Tips

# Organize your code into 'Paragraphs' - capture a complete thought and 'name it'
# Don't repeat yourself - make it work once and then reuse it
# If something gets too long or complex, break it up into chunks, then turn those chunks into functions (maybe build a library).