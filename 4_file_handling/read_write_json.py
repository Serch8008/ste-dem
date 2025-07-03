import json
data = {'a': 1}
with open('file.json', 'w') as f:
    json.dump(data, f)