finput = input('Enter files name: ')

fhand = open(finput, 'r')
for line in fhand:
  line = line.rstrip()
  wds = line.split()
  print(line.upper())

