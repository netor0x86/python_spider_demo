from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
import base64
import json
import requests
import execjs

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.iciba.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.iciba.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}
word = 'hacker'

with open('./iciba.js', 'r') as fp:
    js_code = fp.read()

js_engine = execjs.compile(js_code)
sign = js_engine.call('get_sign', word)

aes1 = AES.new('L4fBtD5fLC9FQw22'.encode(), AES.MODE_ECB)
sign = base64.b64encode(aes1.encrypt(pad(sign.encode(), 16))).decode()

params = {
    'c': 'trans',
    'm': 'fy',
    'client': 6,
    'auth_user': 'key_web_new_fanyi',
    'sign': sign,
}

data = {
    'from': 'en',
    'to': 'zh',
    'q': word,
}

response = requests.post('https://ifanyi.iciba.com/index.php', params=params, headers=headers, data=data)
print(response.text)

# data = "X2NheRsV7GVaBbfK/jxZ6h6rWRz0J268vfthunwKmlJIHB687XwU1lxRMBgI+YF5NDcChW70k1vF0pk7Hi2mTgPICj8jD2YPzqUmeApmXJo/VNvf2rTnfEVD0LgZdP8eIah+O7MzqAmwAxyxWWZ6ysWkf6p5bUFNBfLUvZKMQVy3FmCWe/NkT0FSRS3EL7WediKsKpF8Gq+m/NsT9zVE3sDqIe64/a4F9twH0KVZc+bCH+1eiXP29Po0pKMNkmuhWZN8biNTndn7IEkD1zJKhpTXSl0tJRb87q/u9/l51U5yjeiVxoTCwlOzoZygtiv5OjBE2IuA6V0uGWTyNqP9ku6FgXdPWQacWs1sd6M5I1g="
data = response.json()['content']
key = 'aahc3TfyfCEmER33'

data_db64 = base64.b64decode(data)
aes = AES.new(key.encode(), AES.MODE_ECB)
de_data = aes.decrypt(data_db64)
up_data = unpad(de_data, 16)
json_data = json.loads(up_data)
print(json_data)
