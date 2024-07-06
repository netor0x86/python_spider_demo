import requests
import execjs
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64

session = requests.session()

headers = {
    'accept': 'application/json, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'wdtoken=2acd08fb; __spider__visitorid=50e1f85ab4ad27ee; __spider__sessionid=b4972221c7599d40',
    'origin': 'https://d.weidian.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://d.weidian.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}
response = session.get('https://sso.weidian.com', headers=headers)
wdtoken = response.cookies.get_dict()['wdtoken']

with open('./weidian.js', 'r') as fp:
    js_code = fp.read()

js_engine = execjs.compile(js_code)
ua = js_engine.call('get_ua')
print(ua)


def encrypt(str):
    publicKey = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCvhNi13l0nwSInj/87JeZagQ0PVYTY2IipiLrGLttJLgHH16N3Zpixci6lDgQRWdzomDnNvzD2QFUyVZNjmfmb2fhMDNbzfDktXjSfsNg3NoW85pShlUXLjnggu+OxeJrOYfZT0VFCYzAkbcZKXr+kE+BvvP1eDai8yRib6+PQ9wIDAQAB'
    rsa_pk = RSA.importKey(base64.b64decode(publicKey))
    rsa = PKCS1_v1_5.new(rsa_pk)
    result = rsa.encrypt(str.encode('utf-8'))
    return base64.b64encode(result).decode()


phone = '15012344321'
password = '12345abcd'
countryCode = '86'
data = {
    'phone': encrypt(phone),
    'countryCode': encrypt(countryCode),
    'password': encrypt(password),
    'version': '100',
    'subaccountId': '',
    'clientInfo': '{"clientType":1,"platform":"pc"}',
    'captcha_session': '',
    'captcha_answer': '',
    'vcode': '',
    'mediaVcode': '',
    'ua': ua,
    'scene': 'PCLogin',
    'wdtoken': wdtoken,
}

response = session.post('https://sso.weidian.com/user/login', headers=headers, data=data)
print(response.text)
