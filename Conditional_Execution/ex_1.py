# Grade calculator

def grade():
  score = input('Enter your score from 0.0 to 1.0:')
  try:
    range = float(score)
  except:
    print("Error, please enter number input.")
    quit() # To not continue on (Sanity check)
  
  # This only checks strict values, not ranged values. Happy Path.
  if range == 0.5 :
    print('You super failed!!')
  elif range == 0.6 :
    print('You got an F')
  elif range == 0.7 :
    print('You got a C')
  elif range == 8 :
    print('You got a B')
  elif range == 9 :
    print('You got an A')
  else:
    print('Error, Bad Score')

print(grade())