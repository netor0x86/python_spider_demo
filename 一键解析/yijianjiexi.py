import requests
import execjs
import time

cookies = {
    '__vtins__KPfVVEwb89cQ1LTN': '%7B%22sid%22%3A%20%22c34a3a02-53ad-555c-83c1-61336e9a46ab%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201715389821335%2C%20%22ct%22%3A%201715388021335%7D',
    '__51uvsct__KPfVVEwb89cQ1LTN': '1',
    '__51vcke__KPfVVEwb89cQ1LTN': 'ccc4fb6a-be29-5d6f-988c-4820a72184e5',
    '__51vuft__KPfVVEwb89cQ1LTN': '1715388021339',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__vtins__KPfVVEwb89cQ1LTN=%7B%22sid%22%3A%20%22c34a3a02-53ad-555c-83c1-61336e9a46ab%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201715389821335%2C%20%22ct%22%3A%201715388021335%7D; __51uvsct__KPfVVEwb89cQ1LTN=1; __51vcke__KPfVVEwb89cQ1LTN=ccc4fb6a-be29-5d6f-988c-4820a72184e5; __51vuft__KPfVVEwb89cQ1LTN=1715388021339',
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

'''
function timest() {
    var _0x6a757d = _0x93d9a3
      , _0x51b56a = Date[_0x6a757d(0xed)](new Date())[_0x6a757d(0xf0)]();
    return _0x51b56a = _0x51b56a[_0x6a757d(0xdb)](0x0, 0xa),
    _0x51b56a;
}
js_code = 'function timest() { return Date.parse(new Date()).toString().substr(0, 10) }'
js_engine = execjs.compile(js_code)
t = js_engine.call('timest')
print(t)
'''

t = str(int(time.time()))
print(t)
verify_code = '123456'

with open('yijianjiexi.js', 'r') as fp:
    js_code = fp.read()

js_engine = execjs.compile(js_code)
s = js_engine.call('g', verify_code + t)

print(s)

data = {
    'verify_code': verify_code,
    't': t,
    's': s,
}

response = requests.post('https://www.yijianjiexi.com/api/web/verifyLogin', cookies=cookies, headers=headers, data=data)

print(response.text)
