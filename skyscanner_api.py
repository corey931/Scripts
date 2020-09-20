# install unirest

import requests
import json

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/" \
      "apiservices/browsequotes/v1.0/NL/EUR/nl-NL/" \
      "AMS-sky/" \
      "MAD-sky/" \
      "2020-09-20/" \
      "2020-09-22"

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "a7e4b160a7msh6b0b4d383b8bbbdp15c043jsnf2192b73fee2"
    }

response = requests.request("GET", url, headers=headers)
print(json.dumps(response.json(), sort_keys=True, indent=4))

# https://rapidapi.com/skyscanner/api/skyscanner-flight-search


'''
from skyscanner.skyscanner import Flights
flights_service = Flights('a7e4b160a7msh6b0b4d383b8bbbdp15c043jsnf2192b73fee2')
result = flights_service.get_result(
    country='UK',
    currency='GBP',
    locale='en-GB',
    originplace='SIN-sky',
    destinationplace='KUL-sky',
    outbounddate='2017-05-28',
    inbounddate='2017-05-31',
    adults=1).parsed

print(result)

https://pypi.org/project/skyscanner/
'''