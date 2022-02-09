# Try Block Python

# For elif, if all statements are false, the block should have an else statement as a sort've catch all condition.

# The try/except method works for 'dangerous' code. If the code in the try works - the except is skipped.
# If the code fails the try - it jumps to the except section.

astr = 'Hello Bob'
try:
  istr = int(astr)
except:
  istr = -1
# When the first convention fails - it just drops into the except: clause and the program continues.
print('First', istr)

rtsa = '123'
try:
  rtsi = int(rtsa)
except:
  rtsi = -1
# When the second convention succeeds - it just skips the except: clause and the program continues.
print('Second', rtsi)

