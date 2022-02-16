data = 'X-DSPAM-Confidence: 0.8475 '

atpos = data.find(':')
print(atpos)

sppos = data.find(' ', atpos+2)
print(sppos)

host = data[ atpos+2 : sppos ]
print(host)

indc = type(host)
print(indc)

try:
  takeaway = host.strip()
  # Change to a float
  flyaway = float(takeaway)
  cdni = type(flyaway)
  print(cdni,flyaway)
except:
  print('Unable to convert str to a floating number, please try agian.')

# OR

ipos = data[atpos+2:]
print(ipos)
value = float(ipos)
print(value)