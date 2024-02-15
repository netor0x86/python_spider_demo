import logging
import requests

'''
通过捕获警告到日志的方式忽略警告
'''

logging.captureWarnings(True)
response = requests.get('https://ssr2.scrape.center/', verify=False)
print(response.status_code)
