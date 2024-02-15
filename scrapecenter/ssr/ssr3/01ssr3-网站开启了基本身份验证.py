import requests
from requests.auth import HTTPBasicAuth

'''
网站开启了基本身份验证
'''

# 使用 HTTPBasicAuth
r = requests.get('https://ssr3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
print(r.status_code)

# 不使用 HTTPBasicAuth
r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
print(r.status_code)
