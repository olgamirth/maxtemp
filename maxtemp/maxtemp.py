#!/usr/bin/env python

import requests
import json

lat = 40.99460211262978
lon = -77.56459180420583

api_key = open('/home/dahlberg/PyBites/maxtemp/.tomorrow-io.api-key').read()
api_key = api_key.rstrip()

url = f"https://api.tomorrow.io/v4/weather/forecast?\
location={lat},{lon}&apikey={api_key}"


headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

data = json.loads(response.text)

print(data)
