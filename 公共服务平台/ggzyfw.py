from Crypto.Cipher import AES
import base64
import requests
import time
import execjs

cookies = {
    'ASP.NET_SessionId': '5no0dgole02xvwpkebafm054',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'ASP.NET_SessionId=5no0dgole02xvwpkebafm054',
    'Origin': 'https://ggzyfw.fj.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ggzyfw.fj.gov.cn/guide/index/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    # 'portal-sign': 'a9768d1ba532ad241cd498fd78e6e575',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}
# json_data = {
#     'ts': int(time.time() * 1000),
#     'type': '53',
# }

json_data = {
    'ts': int(time.time() * 1000),
    'type': '35'
}

# json_data = {
#     'IS_IMPORT': 1,
#     'pageSize': 3,
#     'ts': int(time.time() * 1000),
#     'type': "12"
# }

with open('./ggzyfw.js', 'r') as fp:
    js_code = fp.read()

js_engine = execjs.compile(js_code)
s = js_engine.call('d', json_data)
headers['portal-sign'] = s
response = requests.post('https://ggzyfw.fj.gov.cn/FwPortalApi/Article/PageList', cookies=cookies, headers=headers,
                         json=json_data)

key = 'EB444973714E4A40876CE66BE45D5930'
iv = 'B5A8904209931867'
aes = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
enc_str = response.json()['Data']
dec_str = base64.b64decode(enc_str)
str = aes.decrypt(dec_str)
print(str.decode())
