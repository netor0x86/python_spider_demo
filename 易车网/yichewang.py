import requests
import hashlib
import json
import time

cookies = {
    'CIGUID': '5009c71f951b6c5090fd7fe5a62e9e88',
    'auto_id': '01b7ee45732b37b6838efd922aed5970',
    'UserGuid': '5009c71f951b6c5090fd7fe5a62e9e88',
    'selectcity': '140100',
    'selectcityid': '2201',
    'selectcityName': '%E5%A4%AA%E5%8E%9F',
    'CIGDCID': 'H2ihHC4dP4deAjm2bdZ2XJPpKXZWxcns',
    'pageCount': '2',
    'csids': '1729_8108',
    'isWebP': 'true',
    'locatecity': '140100',
    'bitauto_ipregion': '221.205.155.51%3A%E5%B1%B1%E8%A5%BF%E7%9C%81%E5%A4%AA%E5%8E%9F%E5%B8%82%3B2201%2C%E5%A4%AA%E5%8E%9F%E5%B8%82%2Ctaiyuan',
    'Hm_lvt_610fee5a506c80c9e1a46aa9a2de2e44': '1714089239,1714115645,1714351200',
    'Hm_lpvt_610fee5a506c80c9e1a46aa9a2de2e44': '1714351217',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cid': '508',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'CIGUID=5009c71f951b6c5090fd7fe5a62e9e88; auto_id=01b7ee45732b37b6838efd922aed5970; UserGuid=5009c71f951b6c5090fd7fe5a62e9e88; selectcity=140100; selectcityid=2201; selectcityName=%E5%A4%AA%E5%8E%9F; CIGDCID=H2ihHC4dP4deAjm2bdZ2XJPpKXZWxcns; pageCount=2; csids=1729_8108; isWebP=true; locatecity=140100; bitauto_ipregion=221.205.155.51%3A%E5%B1%B1%E8%A5%BF%E7%9C%81%E5%A4%AA%E5%8E%9F%E5%B8%82%3B2201%2C%E5%A4%AA%E5%8E%9F%E5%B8%82%2Ctaiyuan; Hm_lvt_610fee5a506c80c9e1a46aa9a2de2e44=1714089239,1714115645,1714351200; Hm_lpvt_610fee5a506c80c9e1a46aa9a2de2e44=1714351217',
    'origin': 'https://car.yiche.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://car.yiche.com/baoma3xi/peizhi/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-city-id': '2201',
    'x-ip-address': '221.205.155.51',
    'x-platform': 'pc',
    # 'x-sign': '686612b7a5cad180dc953e71abd11630',
    # 'x-timestamp': '1714351216757',
    'x-user-guid': '5009c71f951b6c5090fd7fe5a62e9e88',
}

params = {
    'cid': '508',
    'param': '{"cityId":"2201","serialId":"1729"}',
}


def get_md5(n):
    md5 = hashlib.md5()
    md5.update(n.encode())
    return md5.hexdigest()


timestamp = str(int(time.time() * 1000))
n = f"cid={params['cid']}&param={params['param']}19DDD1FBDFF065D3A4DA777D2D7A81EC{timestamp}"

headers['x-sign'] = get_md5(n)
headers['x-timestamp'] = timestamp

response = requests.get(
    'https://mhapi.yiche.com/hcar/h_car/api/v1/param/get_param_details',
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.text)
