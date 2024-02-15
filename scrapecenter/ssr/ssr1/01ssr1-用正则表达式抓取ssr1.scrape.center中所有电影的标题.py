import requests
import re

'''
抓取 ssr1.scrape.center 中 所有电影的标题
'''

r = requests.get('https://ssr1.scrape.center/')
pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
titles = re.findall(pattern, r.text)
print(titles)
