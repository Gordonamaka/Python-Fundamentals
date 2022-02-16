finput = input('Enter files name: ')

fhand = open(finput)
for line in fhand:
  line = line.rstrip()
  wds = line.split()
  if len(wds) < 3 or wds[0] != 'From' :
    continue
  print(wds[2])

# if the left side of the or is true, it ignores the left condition. Order matters.