import requests
import execjs

cookies = {
    'HWWAFSESTIME': '1713069804144',
    'HWWAFSESID': '63be98eadbcc651ad7',
}

with open('jiansheku.js', 'r') as f:
    js_code = f.read()

js_engine = execjs.compile(js_code)
json_data = {
    'eid': '',
    'achievementQueryType': 'and',
    'achievementQueryDto': [],
    'personnelQueryDto': {
        'queryType': 'and',
    },
    'aptitudeQueryDto': {
        'queryType': 'and',
        'nameStr': '',
        'aptitudeQueryType': 'and',
        'businessScopeQueryType': 'or',
        'filePlaceType': '1',
        'aptitudeDtoList': [
            {
                'codeStr': '',
                'queryType': 'and',
                'aptitudeType': 'qualification',
            },
        ],
        'aptitudeSource': 'new',
    },
    'page': {
        'page': 4,
        'limit': 20,
        'field': '',
        'order': '',
    },
}

result = js_engine.call('get_sign', json_data)

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'HWWAFSESTIME=1713069804144; HWWAFSESID=63be98eadbcc651ad7',
    'Origin': 'https://www.jiansheku.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.jiansheku.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'deviceType': 'PC',
    'page': 'search-enterprise',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sign': result['sign'],
    'timestamp': result['time'],
}

response = requests.post('', cookies=cookies, headers=headers,
                         json=json_data)
print(response.text)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{"eid":"","achievementQueryType":"and","achievementQueryDto":[],"personnelQueryDto":{"queryType":"and"},"aptitudeQueryDto":{"queryType":"and","nameStr":"","aptitudeQueryType":"and","businessScopeQueryType":"or","filePlaceType":"1","aptitudeDtoList":[{"codeStr":"","queryType":"and","aptitudeType":"qualification"}],"aptitudeSource":"new"},"page":{"page":1,"limit":20,"field":"","order":""}}'
# response = requests.post('https://capi.jiansheku.com/nationzj/enterprice/page', cookies=cookies, headers=headers, data=data)
