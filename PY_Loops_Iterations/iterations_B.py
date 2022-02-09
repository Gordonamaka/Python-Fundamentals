# We'll start off with the while loop
n = 5
while n > 0 :
  print(n)
  n = n - 1
print('Blastoff')
print(n, 'Finished')

# To avoid the infinite loop, the variable needs a rate of change to reach a possible 'while' end-point (while n > 0), if this is never true it will always be infinite.

# The break statement ends the current loop and jumps to the statement immediately following the loop
while True:
  line = input('> ')
  if line == 'done' :
    break
  print(line)
print('Done!')

# Finishing an iteration with continue: The continue statement ends the current iteration and jumps to the top of the loop and starts the 'next' iteration
while True:
  line = input('> ')
  if line[0] == '#' :
    continue
  if line == 'done' :
    break
  print(line)
print('Done!')
