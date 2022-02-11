def numreader():
  num = 0
  tot = 0.0
  while True: # Constant true means it'll continue running until false or break.
    sval = input('Enter a Number:') # String Value = sval
    if sval == 'done' :
      break
    try:
      fval = float(sval) # fval means float value
    except:
      print('Invalid input')
      continue
    # print(fval)
    
    num = num + 1 # Counter Pattern
    tot = tot + fval # Cumulator pattern
  print('Finished')
  print(tot,num,tot/num)


print(numreader())



# Order of line orientation matters, you have to order everything logically. What works with what, and when you want it to work is very important.
# try/except accounts for the sanity check.