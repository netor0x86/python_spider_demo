import requests

'''
请求 ssr1.scrape.center 时，添加 User-Agent 请求头
'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81'
}

r = requests.get('https://ssr1.scrape.center/', headers=headers)
print(r.text)
