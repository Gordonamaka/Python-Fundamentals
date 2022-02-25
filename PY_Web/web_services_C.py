# Web Services: JSON

# Python to process JSON - ex.1
import json
data = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "int1",
    "number" : "+1 734 303 4456"
  },
  "email" : {
    "hide" : "yes"
  }
}'''

info = json.loads(data) # Info is a dictionary
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

# Ex.2
input = '''[
  { 
  "id" : "001",
  "x" : "2",
  "name" : "Chuck"
  } ,
  { 
  "id" : "009",
  "x" : "7",
  "name" : "Chuck"
  }
]'''

# Json represents data as nested 'lists" and 'dictionaries' (You can map it into simplier data structures to manipulate).
infotwo = json.loads(input)
print('User count:', len(info))
for item in info:
  print('Name', item['name'])
  print('Id', item['id'])
  print('Attribute', item['x'])