import requests
import pprint
import json

url = "https://avwx.rest/api/metar/"

payload = {}
headers = {
  'Authorization': 'ypCiC7PM9Fg5zn5Ruwc1S1u6q-6Smcvlhh60CyPiXhQ'
}

def CallMETAR(location):
    response = requests.get(url+location, headers=headers)
    return json.loads(response.text)

response_json = CallMETAR('SAEZ')
pprint.pprint(response_json)
print(response_json['sanitized'])
