import json

import requests
from Crypto.Cipher import AES
from Crypto.Util import Padding
import base64

cookies = {
    'wd_guid': '5a734b8d-4d93-4935-80fe-b701b8e88f24',
    'historyState': 'state',
    'R_SCH_CY_V': '3131',
    'W_CITY_S_V': '91',
    '__c': '1715054261',
    '__g': '-',
    '__l': 'l=%2Fwww.kanzhun.com%2F&r=',
    'Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e': '1715054262',
    '__a': '14402582.1706682489.1709525268.1715054261.25.3.2.25',
    'Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e': '1715054265',
    'wbrwsid': '42816714',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    # 'cookie': 'wd_guid=5a734b8d-4d93-4935-80fe-b701b8e88f24; historyState=state; R_SCH_CY_V=3131; W_CITY_S_V=91; __c=1715054261; __g=-; __l=l=%2Fwww.kanzhun.com%2F&r=; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1715054262; __a=14402582.1706682489.1709525268.1715054261.25.3.2.25; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1715054265; wbrwsid=42816714',
    'href': 'https://www.kanzhun.com/search?pageNum=1&query=java&type=5',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.kanzhun.com/search?pageNum=1&query=java&type=5',
    'reqsource': 'fe',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceid': '0d159cfa-c2b0-4171-9129-12534902e69b',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

iv = 'abcdefgh12345678'
str = '{"query": "java", "salaryId": "", "experienceId": "", "pageNum": 1, "limit": 3}'
# str = json.dumps(data)
key = "G$$QawckGfaLB97r"
aes = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
b = base64.b64encode(aes.encrypt(Padding.pad(str.encode(), 16))).decode().replace('/', '_').replace('+', '-').replace(
    '=', '~')

params = {
    'b': b,
    'kiv': iv,
}

response = requests.get('https://www.kanzhun.com/api_to/search/job.json', params=params, cookies=cookies,
                        headers=headers)
aes = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
str = aes.decrypt(base64.b64decode(response.text))
print('str >>>', str.decode())
