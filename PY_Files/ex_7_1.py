finput = input('Enter files name: ')

fhand = open(finput, 'r')
for line in fhand:
  print(line.rstrip().upper())

