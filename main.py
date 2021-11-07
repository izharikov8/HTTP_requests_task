import requests
from pprint import pprint

# Задание 1

names = ['Hulk', 'Captain America', 'Thanos']
intel = 0
for i in names:
    url = f'https://superheroapi.com/api/2619421814940190/search/{i}'
    response = requests.get(url)
    res = response.json()['results']
    for el in res:
        if el['name'] in names:
            a = int(el['powerstats']['intelligence'])
            if a > intel:
                intel = a
                b = el['name']
print(f'Most intelligence character - {b}')


# Задание 2

TOKEN = ''

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    ya = YandexDisk(token = TOKEN)
    ya.upload_file_to_disk('python/netology.txt', 'yadisk.txt')


# Задание 3

def get_files():
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate': '1636156800', 'todate': '1636243200', 'order': 'desc', 'tagged': 'Python', 'site': 'stackoverflow'}
    response = requests.get(url, headers={'Accept': 'application/json'}, params=params)
    return response.json()


pprint(get_files())