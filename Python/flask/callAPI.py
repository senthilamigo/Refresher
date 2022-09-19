#!/usr/bin/python3

import requests
import json

api_url = "http://localhost:5000/param_example"

transaction = { "transId": 1, "transDate": "09/14/2022"}
#headers = {"Content-Type": "application/json"}
#response = requests.get(api_url,params=transaction, headers=headers)

response = requests.get(api_url,params=transaction)

print(response.json())
