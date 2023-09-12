#!/usr/bin/env python
"""

"""

import requests
import json
import logging


def celsius_to_fahrenheit(value: float) -> float:
    return ((value * 1.8) + 32)

class VirtualCrossing_API:
    _forecast_url_template = ("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{},{}?key={}")

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def forecast(self, location: tuple[float, float]) -> dict[list]:
        url = self._forecast_url_template.format(*location, self.api_key)
        headers = {"accept": "application/json"}

        response = requests.get(url, headers)
        response.raise_for_status()

        return response.json()

    @staticmethod
    def max_temp(forecast: dict[list]) -> None:
        tMax = 0
        for day in forecast["days"]:
            print(day["tempmax"])

 



####
#tMax = 0
#for day in data['timelines']['daily']:
#    print(day['values']['temperatureMax'])
#    print(day['time'])
#    if tMax < day['values']['temperatureMax']:
#        tMax = day['values']['temperatureMax']
#        tMaxDay = day['time']
#
#temp = celsius_to_fahrenheit(tMax)
#print(temp)
#print(tMaxDay)
