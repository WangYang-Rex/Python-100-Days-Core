import json

# my_dict = {
#   'name': '骆昊',
#   'age': 38,
#   'qq': 957658,
#   'friends': ['王大锤', '白元芳'],
#   'cars': [
#     {'brand': 'BYD', 'max_speed': 180},
#     {'brand': 'Audi', 'max_speed': 280},
#     {'brand': 'Benz', 'max_speed': 320}
#   ]
# }

# print(json.dumps(my_dict))
# file = open('src/Day21-30/data.json', 'w', encoding='utf-8')
# json.dump(my_dict, file)
# file.close()

file2 = open('src/Day21-30/data.json', 'r', encoding='utf-8')
# data = json.load(file2)
content = file2.read()
data = json.loads(content)
print(type(data))
print(data)
file2.close()

# import requests

# resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
# print(resp.text)