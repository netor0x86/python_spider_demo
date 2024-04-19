import requests
import time
import hashlib
import urllib.parse
import execjs
import httpx

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://souke.xdf.cn',
    'pragma': 'no-cache',
    'referer': 'https://souke.xdf.cn/search?cityCode=110100&kw=%E8%8B%B1%E8%AF%AD',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

timestamp = str(int(time.time() * 1000))

word = '英语'

params = {
    'appId': '5053',
    'cityCode': '110100',
    't': timestamp,
    'pageIndex': '2',
    'pageSize': '12',
    'keyword': urllib.parse.quote(word),
    'order': '0',
}

u = {
    'keyword': urllib.parse.quote(word),
    'order': "0",
    'pageIndex': 2,
    'pageSize': 12
}

t = f"appId=5053&cityCode=110100&t={timestamp}&pageIndex={u['pageIndex']}&pageSize={u['pageSize']}&keyword={u['keyword']}&order={u['order']}750F82C2-D8F6-49F6-878C-1E7EBEBC8DA2"

md5 = hashlib.md5()
md5.update(t.encode())
sign = md5.hexdigest()
print(sign)

with open('loader.js', 'r') as fp:
    js_code = fp.read()

js_engine = execjs.compile(js_code)
sign = js_engine.call('getSign', t)
print(sign)
headers['Sign'] = sign

response = httpx.get('https://dsapi.xdf.cn/product/v2/class/search', params=params, headers=headers)
print(response.text)
