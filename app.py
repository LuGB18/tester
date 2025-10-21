import requests
import os
import json
from threading import Thread

if os.path.exists('config.ini'):
    with ('config.ini', 'r') as config:
        config = json.loads(config)
else:
    key = requests.get("https://raw.githubusercontent.com/LuGB18/tester/refs/heads/main/key.json").json()
    essential = requests.get("https://raw.githubusercontent.com/LuGB18/tester/refs/heads/main/update.json").json()
    essential['key'] = key['key']
    with open('config.ini', 'w') as config:
        json.dump(essential, config)

try:
    key = config['key']
except Exception as e:
    print(f'Unable to load nessesary variables, please, contact the repo owner or\npost on the troubleshoots tab on the repo:')
    



