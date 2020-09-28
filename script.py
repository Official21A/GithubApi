'''
	This is a simple script to send a request to a URL
	and get the response.
	The url inuse has an API that returns json format data.
'''

import requests


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers) # this is how we send our requests

print(f'Status code: {r.status_code}')

response_dict = r.json() # it reads all the json data

print(response_dict.keys())