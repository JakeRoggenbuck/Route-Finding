import requests
import json
import api_key

from_location = input("From: ")
to_location = input("To: ")

api_url = f'origin={from_location}+ON&destination={to_location}+ON'
full_url = f'https://maps.googleapis.com/maps/api/directions/json?units=imperial&{api_url}&key={api_key.key}'
request = requests.get(full_url)
info = request.json()

print(info)
