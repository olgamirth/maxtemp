#!/usr/bin/env python

import requests
import json


def c2F(celsius: float) -> "float":
    return ((celsius * 1.8) + 32)


lat = 40.99460211262978
lon = -77.56459180420583

api_key = open('/home/dahlberg/PyBites/maxtemp/.tomorrow-io.api-key').read()
api_key = api_key.rstrip()

url = f"https://api.tomorrow.io/v4/weather/forecast?\
location={lat},{lon}&apikey={api_key}"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

data = json.loads(response.text)

tMax = 0
for day in data['timelines']['daily']:
    if tMax < day['values']['temperatureMax']:
        tMax = day['values']['temperatureMax']
        tMaxDay = day['time']

temp = c2F(tMax)
print(temp)
print(tMaxDay)
