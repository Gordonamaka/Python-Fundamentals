# Comparison operators
# < Less than
# <=  Less than or equal to
# > Greater than
# >= Greater than or equal to
# > greater than
# != not equal

# Indentation is very import in python

# Three indentation rules of thumb: 
# Increase indent, indent after an if statement or for statement (after :)
# Maintain indent to indicate the scope of the block (white lines are affected by the if/for)
# Reduce indent back to the level of the if statement or for statement to indicate the end of the block

# You Deindent for if-else statements
x  = 2
if x > 2 :
  print('Bigger')
else :
  print('Smaller')
  
print('All Done')

# 'else if' is 'elif' in python
# Interestingly enough, elif statements actually matter in python. If you were to make the elif an if statement, it would print all that apply. Else however is the catch all, without it, it could return nothing.
l = 1
if l < 2 :
  print('Small')
elif l < 10 :
  print('Medium')
else :
  print('Large')
print('All done')

