# Definite Loops only run a finite number of times.
# i is the iteration variable ( it 'iterates' through the sequence (ordered set)). The block body - print(i) - of code is executed once for each value in the sequence.
# iteration variable (i) moves through all of the values in the sequence. Five-element sequence in the array. 
for i in [5, 4, 3, 2, 1] :
  print(i) 
# If you leave the second print function in the for loop block, it will print 'Loop complete' with every iteration.
print('Loop complete.')

friends = ['Joseph', 'Michael', 'Bay']
for friend in friends :
  print('It turns out ' + friend + ' has a terminal illness') # Adds the strings with the variable.
  # You can format with formatted string literals but it seems more complicated than string concaternation. (Research more).
print('Complete')