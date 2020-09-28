# continue

import requests
from plotly.graph_objs import Bar
from plotly import offline


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' # main url
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers) # this is how we send our requests

print(f'Status code: {r.status_code}') # getting the response status code

response_dict = r.json() # it reads all the json data
repo_dicts = response_dict['items'] # a dictionary of repositories
repo_links, stars, labels = [], [], []

for repo_dict in repo_dicts:
	# creating a link type html for the xaxises
	repo_name = repo_dict['name']
	repo_url = repo_dict['html_url']
	repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
	repo_links.append(repo_link)
	# starts as yaxises
	stars.append(repo_dict['stargazers_count'])
	# owere infor for hover text
	owner = repo_dict['owner']['login']
	description = repo_dict['description']
	label = f'{owner}<br />{description}'
	labels.append(label)


# just like working with data we use bar to show the results of responce
data = [{
	'type': 'bar',
	'x': repo_links,
	'y': stars,
	'hovertext': labels,
	'marker': {
		'color': 'rgb(60, 100, 150)',
		'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
	},
	'opacity': 0.6,
}]	

my_layout = {
	'title': 'Most-Starred Python Projects on Github',
	'titlefont': {'size':28},
	'xaxis': {
		'title': 'Repository',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
	'yaxis': {
		'title': 'Stars',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html') # saving file into *.html