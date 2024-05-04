import requests
import execjs

with open('wencaiwang.js', 'r') as fp:
    js_code = fp.read()

js_engine = execjs.compile(js_code)
v = js_engine.call('get_v')

cookies = {
    'other_uid': 'Ths_iwencai_Xuangu_qyv44x1elfbv4zuh0ovgxxeftb6nvnv4',
    'ta_random_userid': 'g5bp7mkkqp',
    'cid': '0a1404b12036f431618c529e627876401714360900',
    'v': v,
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'other_uid=Ths_iwencai_Xuangu_qyv44x1elfbv4zuh0ovgxxeftb6nvnv4; ta_random_userid=g5bp7mkkqp; cid=0a1404b12036f431618c529e627876401714360900; v=A-u9T8WMCR1jrlXJXxllYfGqfATQAP_8eRTDOF1oxyqB_AX65dCP0onkU5du',
    'Origin': 'https://www.iwencai.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.iwencai.com/unifiedwap/result?w=%E4%BB%8A%E6%97%A5%E6%B6%A8%E5%81%9C&querytype=stock',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'hexin-v': v,
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data = {
    'query': '今日涨停',
    'urp_sort_way': 'desc',
    'urp_sort_index': '涨停[20240429]',
    'page': '1',
    'perpage': '50',
    'addheaderindexes': '',
    'condition': '[{"dateText":"今日","indexName":"涨停","indexProperties":["交易日期 20240429"],"ci":true,"dateUnit":"日","source":"text2sql","type":"index","indexPropertiesMap":{"交易日期":"20240429"},"reportType":"TRADE_DAILY","ciChunk":"今日涨停","score":0.0,"createBy":"preCache","dateType":"交易日期","isExtend":false,"chunkedResult":"今日涨停","uiText":"今日的涨停","valueType":"_是否","domain":"abs_股票领域","sonSize":0,"logid":"8815ebfe06ec3d73cfad8e240283410b","dateList":["今日"],"order":0}]',
    'codelist': '',
    'indexnamelimit': '',
    'logid': '8815ebfe06ec3d73cfad8e240283410b',
    'ret': 'json_all',
    'sessionid': '8815ebfe06ec3d73cfad8e240283410b',
    'source': 'Ths_iwencai_Xuangu',
    'date_range[0]': '20240429',
    'iwc_token': '0ac9665717143609509372073',
    'urp_use_sort': '1',
    'user_id': 'Ths_iwencai_Xuangu_qyv44x1elfbv4zuh0ovgxxeftb6nvnv4',
    'uuids[0]': '24087',
    'query_type': 'stock',
    'comp_id': '6836372',
    'business_cat': 'soniu',
    'uuid': '24087',
}

response = requests.post('https://www.iwencai.com/gateway/urp/v7/landing/getDataList',
                         cookies=cookies, headers=headers,
                         data=data)
print(response.json())
