import requests
import json

URL = ""

data = {
    'name' : 'Abhi',
    'roll' : 101,
    'city' : 'surat'
}

json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)
