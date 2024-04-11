import requests
import execjs

cookies = {
    'PHPSESSID': 'j6pohjeuaoutdnfu353c0ovup2',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    # 'Cookie': 'PHPSESSID=j6pohjeuaoutdnfu353c0ovup2',
    'Origin': 'https://www.maomaozu.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.maomaozu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

with open('maomaozu.js', 'r') as fp:
    js_code = fp.read()

js_engine = execjs.compile(js_code)
data = js_engine.call('get_encrypt', 1)

response = requests.post('https://www.maomaozu.com/index/build.json', cookies=cookies, headers=headers, data=data)
# print(response.text)

print(js_engine.call('aes_decrypt', response.text))
