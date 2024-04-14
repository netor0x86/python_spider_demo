import requests
from urllib.parse import quote
import execjs

headers = {
    'accept': 'text/plain, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://search.bidcenter.com.cn',
    'pragma': 'no-cache',
    'referer': 'https://search.bidcenter.com.cn/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

keyword = '存储'

data = {
    'from': '6137',
    'guid': '26c967fa-da07-42cf-ad53-40dac90ebf00',
    'location': '6138',
    'token': '',
    'next_token': '',
    # 'keywords': '%E6%9C%8D%E5%8A%A1%E5%99%A8',
    'keywords': quote(keyword),
    'mod': '0',
    'page': '2',
}

response = requests.post('https://interface.bidcenter.com.cn/search/GetSearchProHandler.ashx', headers=headers,
                         data=data)
# print(response.text)

with open('caizhaowang.js', 'r') as f:
    js_code = f.read()

js_engine = execjs.compile(js_code)
print(js_engine.call('AESDecrypt', response.text))
