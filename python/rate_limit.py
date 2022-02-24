import requests
import os
from datetime import datetime

request = requests.get(f'https://api.github.com/rate_limit', auth=('Kiptoke',os.getenv('token'))).json()['resources']['core']

used = request['used']
limit = request['limit']
date = datetime.fromtimestamp(request['reset'])
print(f'{used} uses out of {limit}')
print(f'API rate limit resets at {date}')