import json
with open("dataTK.json", "r", encoding='utf-8') as f:
    db = json.load(f)
for data in db:
    for key,value in data.items():
       tk = data["user"]
       mk = data["password"]
