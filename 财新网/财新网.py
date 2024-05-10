import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import urllib.parse

cookies = {
    'ENTITY_ID': '',
    'CX_FROM': 'null',
    'GUID': '226981867',
    'T_GUID': '1715301765706',
    'GID30': '226981867',
    'point': '1715356799000',
    'FROM_CHINA': 'true',
    'gr_user_id': 'a1021630-a96b-4108-a9e2-88b461d6ca4b',
    '872f3eaac31f373e_gr_session_id': '2f74412f-4a15-49e2-b323-35c377c28f69',
    '872f3eaac31f373e_gr_session_id_sent_vst': '2f74412f-4a15-49e2-b323-35c377c28f69',
    'lastTime': '1715301821473',
    'firstTime': '1715301821473',
    'ENTITY_COUNT': '2',
    'sidebarStatus': '1',
    'LOGIN_QR_CODE': 'Cimew8dth991pzaGbloFtVznTBiAABTN',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'ENTITY_ID=; CX_FROM=null; GUID=226981867; T_GUID=1715301765706; GID30=226981867; point=1715356799000; FROM_CHINA=true; gr_user_id=a1021630-a96b-4108-a9e2-88b461d6ca4b; 872f3eaac31f373e_gr_session_id=2f74412f-4a15-49e2-b323-35c377c28f69; 872f3eaac31f373e_gr_session_id_sent_vst=2f74412f-4a15-49e2-b323-35c377c28f69; lastTime=1715301821473; firstTime=1715301821473; ENTITY_COUNT=2; sidebarStatus=1; LOGIN_QR_CODE=Cimew8dth991pzaGbloFtVznTBiAABTN',
    'Pragma': 'no-cache',
    'Referer': 'https://u.caixin.com/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

password = '123456abcd'
key = 'G3JH98Y8MY9GWKWG'
aes = AES.new(key.encode(), AES.MODE_ECB)
enc_password = base64.b64encode(aes.encrypt(pad(password.encode(), 16)))
# print(enc_password)

params = {
    'account': '15011223344',
    'password': urllib.parse.quote(enc_password),
    'deviceType': '5',
    'unit': '1',
    'areaCode': '+86',
    'callback': '__caixincallback1715301849323',
}

response = requests.get(
    'https://gateway.caixin.com/api/ucenter/user/v1/loginJsonp',
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.text)
