import json

data = '''
[

  { 
  "id": "001",
  "x": "2",
  "name": "Chuck"
  },

  { 
  "id": "009",
  "x":  "7",
  "name": "Bruno"
  }

]
'''

info = json.loads(data)
print('User count:', len(info))
print(info[1])
# for item in info:
#     print()
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])
#     print()
