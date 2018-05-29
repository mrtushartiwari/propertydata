import json

with open('data2.json') as json_data:
    d = json.load(json_data)
    print(d["area1"])