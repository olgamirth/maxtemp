#!/usr/bin/env python

import requests
import json


def celsius_to_fahrenheit(value: float) -> float:
    return ((value * 1.8) + 32)


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
    print(day['values']['temperatureMax'])
    print(day['time'])
    if tMax < day['values']['temperatureMax']:
        tMax = day['values']['temperatureMax']
        tMaxDay = day['time']

temp = celsius_to_fahrenheit(tMax)
print(temp)
print(tMaxDay)
