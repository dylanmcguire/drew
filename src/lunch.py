print("Hey its lunch time!")

alias = input('What are you hungry for today?')
print('Wise choice',alias, 'it is!')

import json
import urlib
import argparse
import pprint
import

from urllib.error import HTTPError


api_key = 'CA2ee83TZpJ30w5RD5fIVymGMPYAGV77kDiU1zw7UzAuYem52gH5Vyk6SNi9YTLJ1m8UL5d20J7SJv6SVPe4iXmkw69w6grmRgPUTsUAg9gUqvmnDWSDXdV_atsGW3Yx'
url = 'https://api.yelp.com/v3/categories/search'
headers = {'Authorization': 'Bearer api_key'}
url_params = {'latitude': 39.98, 'longitude':
    -82.98, 'radius': 2500, 'term': 'restaurant'}

def request(url, url_params, headers):
    response = requests.request('GET', url, headers=headers, url_params=url_params)
    return response.json()