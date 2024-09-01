import requests
import json
import pprint

url = "http://localhost:8000/api/test"

data = {
    "message": "明日の18時から電通大のC403で部会をやる",
}

response = requests.post(url, json=data)

res_json = json.loads(response.text)
pprint.pprint(res_json)
