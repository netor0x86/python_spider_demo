import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
import base64

cookies = {
    'lianjia_uuid': '0374268c-ad3c-46c1-9171-1a323b4d77c5',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218eea6ed1c7e8a-0c016fe79427f2-1c525637-2073600-18eea6ed1c88fe%22%2C%22%24device_id%22%3A%2218eea6ed1c7e8a-0c016fe79427f2-1c525637-2073600-18eea6ed1c88fe%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wybeijing%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D',
    'select_city': '110000',
    'lianjia_ssid': '36b802b1-3682-40a5-87e8-e31772de8f9c',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://bj.ke.com',
    'Pragma': 'no-cache',
    'Referer': 'https://bj.ke.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

json_data = {
    'service': 'https://ajax.api.ke.com/login/login/getuserinfo',
    'version': '2.0',
}

response = requests.post('https://clogin.ke.com/authentication/initialize', cookies=cookies, headers=headers,
                         json=json_data)

loginTicketId = response.json()['loginTicketId']


def get_key():
    PublicKey = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCCB81pk1Go/d7K8unYqeB6YyQdDgIRsLji7BxlBfMC2U8/0lyOLxJ6sQb1RmKaILuxN0hRci4zWPfkkPhttWaogq3XABYiDYbx0843ge4D79pG21+qWplw43uHZNs0B6iUChJW1O3DDJPXGwj50L1ySTVt7G7iqsIr9PLZVRSZmQIDAQAB'
    data = base64.b64decode(PublicKey)
    key = RSA.importKey(data)
    return key


def encrypt_data(msg):
    public_key = get_key()
    cipher = PKCS1_cipher.new(public_key)
    encrypt_text = base64.b64encode(cipher.encrypt(msg.encode()))
    return encrypt_text.decode()


password = encrypt_data('1234567890')

json_data = {
    'service': 'https://ajax.api.ke.com/login/login/getuserinfo',
    'mainAuthMethodName': 'username-password',
    'accountSystem': 'customer',
    'credential': {
        'username': '15011112222',
        'password': password,
        'encodeVersion': '1',
    },
    'context': {
        'ua': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'clientSource': 'pc',
        'os': 'Mac OS',
        'osVersion': '10.15.7',
        'registerPosLx': 625.5,
        'registerPosLy': 159.5,
        'registerPosRx': 905.5,
        'registerPosRy': 203.5,
        'clickPosX': 726,
        'clickPosY': 185,
        'screen': '1292_266',
        'dataId': 'XlJ/b0ZLDVIFQltHO7H9Z+rI/KLMDwAJAfa0rdsnqSdv0Ywj9iN6ckzyf/UNTzKQ',
    },
    'loginTicketId': loginTicketId,
    'version': '2.0',
    'srcId': 'eyJ0Ijoie1wiZGF0YVwiOlwiZDIwMGQ4MzJhOTU3NTcxNzc3ZWUwNzU2ZGU0NDdjZDBlZGY2MmJlMzA2YWNiODNkNjE4OGVjMzVlOGM2N2VlMTdhZDY5N2EyZTZiYmYwMWY0N2NlNzhhMzJlZDgzYmZmZDFlOTQ0YmI5MGFmMDc5NDNkZjY0NjcwNzhkOTU4NGY3ODJmMzdkNWVkNjQ2MTlkY2E5MmQxNzA3ODNkM2M1MDAyYzkyMmNhMzdlZWYyZDM2MGU2MTRkOWMyY2JmNzUxYjk4MjJmZTliMGUxOTZkNDg3NzQxMGMxYTczNjU4NTU2ZTJlMGNkMDBhNmYwNWVjNzA0OTgyNjM5NWMxYjdkMlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI5OGEwYjA0NFwifSIsInIiOiJodHRwczovL2JqLmtlLmNvbS8/dXRtX3NvdXJjZT1iYWlkdSZ1dG1fbWVkaXVtPXBpbnpodWFuJnV0bV90ZXJtPWJpYW90aSZ1dG1fY29udGVudD1iaWFvdGltaWFvc2h1JnV0bV9jYW1wYWlnbj13eWJlaWppbmciLCJvcyI6IndlYiIsInYiOiIwLjEifQ==',
}

response = requests.post('https://clogin.ke.com/authentication/authenticate',
                         cookies=cookies,
                         headers=headers,
                         json=json_data)
print(response.text)
