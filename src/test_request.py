# pip install requests
import random
import requests


username = 'PROXY_USERNAME'
password = 'PROXY_PASSWORD'
proxy = 'proxy-endpoint:60000'

if not username.endswith('-test'):
    username += '-test'

proxies = {
    'http': f'http://{username}:{password}@{proxy}',
    'https': f'http://{username}:{password}@{proxy}'
}

response = requests.get(
    'https://ip.oxylabs.io/location',
    proxies=proxies
)
print(response.json())