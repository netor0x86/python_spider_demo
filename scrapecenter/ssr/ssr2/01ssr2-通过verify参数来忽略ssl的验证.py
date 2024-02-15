import requests
from requests.packages import urllib3

'''
通过 verify 参数来忽略 ssl 的验证
通过 urllib3.disable_warnings() 来屏蔽警告
'''

urllib3.disable_warnings()
response = requests.get('https://ssr2.scrape.center/', verify=False)
print(response.status_code)
