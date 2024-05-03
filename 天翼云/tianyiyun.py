import requests
import execjs

with open('./tianyiyun.js', 'r') as fp:
    js_code = fp.read()

js_engine = execjs.compile(js_code)

comParam_curTime = js_engine.call('get_com_param_cur_time')
comParam_seqCode = js_engine.call('get_com_param_seq_code')
comParam_signature = js_engine.call('get_com_param_signature', comParam_curTime, comParam_seqCode)

cookies = {
    'ct_m_dvc_id': '903dacbe8891e05d87544f4af62641e5',
    'sid1': '1714740900248-509FE8CC0EC46414E4DA7628CC0CB805',
    'sid2': '1714740900248-509FE8CC0EC46414E4DA7628CC0CB805',
    'pvid': '1',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'ct_m_dvc_id=903dacbe8891e05d87544f4af62641e5; sid1=1714740900248-509FE8CC0EC46414E4DA7628CC0CB805; sid2=1714740900248-509FE8CC0EC46414E4DA7628CC0CB805; pvid=1',
    'Origin': 'https://m.ctyun.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://m.ctyun.cn/wap/main/auth/login?redirect=%2Fmy',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'x-riskdevicesign': '903dacbe8891e05d87544f4af62641e5',
}

params = {
    'referrer': 'wap',
    'mainVersion': '300031500',
    # 'comParam_curTime': '1714741417080',
    'comParam_curTime': comParam_curTime,
    # 'comParam_seqCode': '2A355DEF1130A845502AD5B61E277792',
    'comParam_seqCode': comParam_seqCode,
    # 'comParam_signature': '94a065b7af6e1b177e44a9c1c75f6e2b',
    'comParam_signature': comParam_signature,
    'isCheck': 'true',
    'locale': 'zh-cn',
}

username = '15512344321@163.com'
password = '12345asdf'
enc_password = js_engine.call('get_password', password, username)

data = {
    'userName': username,
    'password': enc_password,
    'authCode': '',
}

response = requests.post('https://m.ctyun.cn/account/login', params=params, cookies=cookies, headers=headers, data=data)
print(response.text)
