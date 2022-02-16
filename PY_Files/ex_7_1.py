finput = input('Enter files name: ')

fhand = open(finput)
for line in fhand:
  line = line.rstrip()
  print('Line:', line)
  if line == '' :
    print('Skip Blank')
    continue
  wds = line.split()
  print('Words:', wds)
  if wds[0] != 'From' :
    print('Ignore')
    continue
  print(wds[2])

