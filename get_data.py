import pandas as pd
import numpy as np
import json
import requests

#Retrieving my api keys information to access the Google API.
def get_keys(path):
    with open(path) as f:
        return json.load(f)
    
keys = get_keys("/Users/jjherranzsarrion/.secret/google_blog2_api.json")
api_key = keys['api_key']

url = 'https://maps.googleapis.com/maps/api/directions/json?'

origin = 'Sheepfold+Dog+Park+Fells+Path+Stoneham+MA'
destination = 'Terminal+C+Boston+Logan+International+Airport+Boston+MA+02128'
departure_time = '1566819000' #time in seconds from midnight 1st Jan 1970 (Unix start time) until Monday 19th August at 07:30 AM. 
 
url_params = f"origin={origin}&destination={destination}&departure_time={departure_time}&key={api_key}"

request_url = url + url_params
      
response = requests.get(request_url)

with open('response.json', 'w') as f:
    json.dump(response.json(), f)
