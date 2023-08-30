#!/usr/bin/env python

import requests

lat = 40.99460211262978
long = -77.56459180420583

api_key = open('/home/dahlberg/PyBites/maxtemp/.tomorrow-io.api-key').read()

print(api_key)

url = f"https://api.tomorrow.io/v4/weather/forecast?\
location={lat},{long}&apikey={api_key}"

print(url)

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
