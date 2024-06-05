import requests
import execjs

with open('./huinong2.js', 'r') as fp:
    js_code = fp.read()

js_engine = execjs.compile(js_code)
header = js_engine.call('get_header')
print('python sign:', header)

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://m.cnhnb.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://m.cnhnb.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    
}

headers.update(header)

json_data = {
    'pageNumber': 2,
    'pageSize': 8,
    'ad_ch': 1,
}

response = requests.post('https://appapi.cnhnb.com/recq/api/transform/supply/v501/index', headers=headers,
                         json=json_data)

print('result --->', response.text)
