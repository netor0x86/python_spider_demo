import requests

'''
获取 scrape.center 的 favicon.ico 图标
'''

r = requests.get('https://scrape.center/favicon.ico')
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
