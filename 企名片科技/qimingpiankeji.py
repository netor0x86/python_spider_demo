import requests
import execjs

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.qimingpian.com',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

data = {
    'unionid': '',
}

response = requests.post('https://vipapi.qimingpian.cn/HomePage/recommendInfo', headers=headers, data=data)
# print(response.text)

with open('qimingpiankeji.js', 'r') as f:
    js_code = f.read()

js_engine = execjs.compile(js_code)
print(js_engine.call('decrypt', response.text))
