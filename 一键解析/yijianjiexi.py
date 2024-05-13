import requests
import execjs
import time

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.yijianjiexi.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

t = str(int(time.time()))

verify_code = '123456'

with open('./yijianjiexi.js', 'r') as fp:
    js_code = fp.read()

js_engine = execjs.compile(js_code)
s = js_engine.call('g', verify_code + t)

data = {
    'verify_code': verify_code,
    't': t,
    's': s,
}
print(len(s), ',', s)
response = requests.post('https://www.yijianjiexi.com/api/web/verifyLogin', headers=headers, data=data)

print(response.text)
