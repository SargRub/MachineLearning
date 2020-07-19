import requests
import json

info = requests.get('https://swapi.dev/api/people')

json_text = info.json()

with open('file.json', 'w') as json_file:
    json.dump(json_text, json_file, indent=4)

