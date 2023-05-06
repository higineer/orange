import json

# python dictionary

customer = {
    'id': 1123,
    'name': 'higineer',
    'history': [
        {'date': '2022-05-13', 'spec': 'm.2'},
        {'date': '2023-05-02', 'spec': 'ufs'},
    ]
}

# json encoding: python data -> json string
# jsongString = json.dumps(customer)
jsongString = json.dumps(customer, indent=4)

# print string
print(jsongString)
print(type(jsongString)) # class str

# json decoding: json string -> python data
dic = json.loads(jsongString)
print(type(dic))
print(dic['name'])
for h in dic['history']:
    print(h['date'], h['spec'])