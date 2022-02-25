# Web Services: API Rate limiting and Security

# Twitter's API for example requires account authentication

import urllib.request, urllib.parse, urllib.error
import twurl # For Twitter security (pip package)
import json

# Accessing a friends list
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json' # constants are written in all capital letters and underscores separating the words. A type of variable whose value cannot be changed.(Python)

while True:
  print('')
  acct = input('Enter Twitter Account: ')
  if (len(acct) < 1): break
  url = twurl.augment(TWITTER_URL, 
                      {'screen_name': acct, 'count': '5'})
  print('Retrieving', url)
  connection = urllib.request.urlopen(url)
  data = connection.read().decode() # Solves UTF-8
  headers = dict(connection.getheaders())
  print('Remaining', headers['x-rate-limit-remaining'])
  js = json.loads(data) # Deserialize
  print(json.dumps(js, indent=4)) # Serialize
  
  for u in js['users']:
    print(u['screen_name'])
    s = u['status']['test']
    print('  ', s[:50])