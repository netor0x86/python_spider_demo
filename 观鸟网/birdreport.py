import requests
import execjs
from urllib.parse import urlencode
import base64
from Crypto.Cipher import AES

with open('birdreport.js', 'r') as f:
    js_code = f.read()

js = execjs.compile(js_code)
param = {
    'page': 1,
    'limit': 20
}
ret = js.call('beforeSend', urlencode(param))

encrypt_data = ret['encrypt_data']

url = 'https://api.birdreport.cn/front/record/activity/search'

headers = {
    'Timestamp': ret['headers']['Timestamp'],
    'Requestid': ret['headers']['Requestid'],
    'Sign': ret['headers']['Sign'],
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Referer': 'http://birdreport.cn/',
}

session = requests.session()
session.headers.update(headers)
response = session.post(url, encrypt_data)

iv = 'd93c0d5ec6352f20'.encode()
key = '3583ec0257e2f4c8195eec7410ff1619'.encode()

aes = AES.new(key, AES.MODE_CBC, iv)
decrypted_data = aes.decrypt(base64.b64decode(response.json()['data']))
print(decrypted_data.decode())
