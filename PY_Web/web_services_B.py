# XML Schema

"""
Description of the legal format of an xml document

Expressed in terms of constraints on the structure and content of documents

Often used to specify a "contract" between systems - "My system will only accept XML that conforms to this particular Schema."

If a particular piece of XML meets the specification of the Schema - it is said to "validate"
"""

# Example 1
import xml.etree.ElementTree as ET
data = '''<person>
<name>Chuck</name>
<phone type="int1">
+1 734 3030 4456
</phone>
<email hide="yes" />
<person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))


# Example 2
input = '''<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
  print('Name', item.find('name').text)
  print('Id', item.find('id').text)
  print('Attribute', item.get("x"))
