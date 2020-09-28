# continue

import requests


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers) # this is how we send our requests

print(f'Status code: {r.status_code}')

response_dict = r.json() # it reads all the json data

print(f'Total repositories: {response_dict["total_count"]}') # total amount of the repos with python

repo_dicts = response_dict['items'] # a dictionary of repositories
print(f'Repositories returned: {len(repo_dicts)}')

repo_dict_0 = repo_dicts[0] # getting the first item
print(f'\nKeys: {len(repo_dict_0)}')
for key in sorted(repo_dict_0.keys()):
	print(key)

print('\nSelected information about each repository:') # then we print some of the infomration of the results
for repo_dict in repo_dicts:
	print(f'Name: {repo_dict["name"]}')
	print(f'Owner: {repo_dict["owner"]["login"]}')
	print(f'Stars: {repo_dict["stargazers_count"]}')
	print(f'Repository: {repo_dict["html_url"]}')	
	print(f'Created: {repo_dict["created_at"]}')
	print(f'Updated: {repo_dict["updated_at"]}')
	print(f'Description: {repo_dict["description"]}')


'''
	So each api has a limit for requests per minute.
	In this case we can see out status in limitaion via 
	https://api.github.com/rate_limit.
	Each url api has its own limits.
'''	
