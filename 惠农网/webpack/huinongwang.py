import requests
import execjs

with open('huinongwang.js', 'r') as fp:
    js_code = fp.read()

js_engine = execjs.compile(js_code)

time = js_engine.call('get_time')
print('time:::', time)

nonce = js_engine.call('get_nonce')
print('nonce:::', nonce)

trace_id = js_engine.call('get_trace_id')
print('trace_id:::', trace_id)

sign = js_engine.call('get_sign', time, nonce, trace_id)
print('sign:::', sign)
# X-B3-TraceId
# X-Client-Nonce
# X-Client-Sign
# X-Client-Time

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://m.cnhnb.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://m.cnhnb.com/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-b3-traceid': trace_id,
    'x-client-appid': '5',
    'x-client-environment': 'pro',
    'x-client-id': '10bc3b4-d6a3-4ac3-8bd0-e10ca1b7a',
    # 'x-client-nonce': '801c1255903a89b6d5ac0df854d8f5cc',
    'x-client-nonce': nonce,
    'x-client-page': '/',
    'x-client-sid': 'S_0LV9BTVAUVZW1MPM',
    # 'x-client-sign': '515f3c23fdc2b525243e31af9844a500f39f9c847650536515a1a475446811b6586af77444493e88cf03b8ccc742d712',
    'x-client-sign': sign,
    # 'x-client-time': '1713691766684',
    'x-client-time': time,
    'x-hn-job': 'If you see these message, I hope you dont hack us, I hope you can join us! Please visit https://www.cnhnkj.com/job.html',
}

json_data = {
    'pageNumber': 12,
    'pageSize': 8,
    'ad_ch': 1,
}

response = requests.post('https://appapi.cnhnb.com/recq/api/transform/supply/v501/index', headers=headers,
                         json=json_data)
print(response.text)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{"pageNumber":12,"pageSize":8,"ad_ch":1}'
# response = requests.post('https://appapi.cnhnb.com/recq/api/transform/supply/v501/index', headers=headers, data=data)
