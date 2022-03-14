import requests
from pprint import pprint

# Задание 3
url = 'http://api.stackexchange.com/2.3/questions?fromdate=1647043200&todate=1647216000&order=desc&sort=activity&tagged=Python&site=stackoverflow'
response = requests.get(url)
data_dict = {}
for el in response.json()['items']:
    data_dict[el['title']] = el['link']
pprint(data_dict)