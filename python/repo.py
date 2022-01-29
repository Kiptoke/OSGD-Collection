import requests
import json
from variables import auth

with open('repos/aseprite.txt', 'w') as file:
    r = requests.get('https://api.github.com/repos/aseprite/aseprite', auth=('kiptoke',auth.get('github')))
    file.write(json.dumps(r.json(), indent=4))