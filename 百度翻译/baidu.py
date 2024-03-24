import requests
import execjs

cookies = {
    'REALTIME_TRANS_SWITCH': '1',
    'FANYI_WORD_SWITCH': '1',
    'HISTORY_SWITCH': '1',
    'SOUND_SPD_SWITCH': '1',
    'SOUND_PREFER_SWITCH': '1',
    'PSTM': '1706284751',
    'BIDUPSID': 'C117306D69C3E4BA008A25BB285CFF61',
    'BAIDUID': 'B7F72B04A4AC4F87C74E337AC724C546:FG=1',
    'BAIDUID_BFESS': 'B7F72B04A4AC4F87C74E337AC724C546:FG=1',
    'H_PS_PSSID': '40043_39996',
    'ZFY': 'buvjvWr:A5pJSYcdGIsh2:Agz68HPe8p1BOB:B88lsz7Ss:C',
    'PSINO': '5',
    'delPer': '0',
    'H_WISE_SIDS': '40043_39996',
    '__bid_n': '18cb89f28523728c425b1d',
    'BDUSS': 'UV4fnVhNHV2Z09jTHRsandjYXNBamNJNVRXRW8tLTNzMW9udDBSMGZGVWlpOXhsRUFBQUFBJCQAAAAAAAAAAAEAAADG8h9UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACL-tGUi~rRlR',
    'BDUSS_BFESS': 'UV4fnVhNHV2Z09jTHRsandjYXNBamNJNVRXRW8tLTNzMW9udDBSMGZGVWlpOXhsRUFBQUFBJCQAAAAAAAAAAAEAAADG8h9UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACL-tGUi~rRlR',
    'BDRCVFR[feWj1Vr5u3D]': 'I67x6TjHwwYf0',
    'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1705500161,1706450163',
    'RT': '"z=1&dm=baidu.com&si=92452f11-b0b3-4ea2-a6f3-b89a8acb7ac6&ss=lrywzoc1&sl=n&tt=6f6&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2i4dk&ul=2jghk&hd=2jgix"',
    'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1706621472',
    'APPGUIDE_10_6_9': '1',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Acs-Token': '1706612760002_1706621537324_n37wmN5rGXcLv5ONmXVmqTqvBZgQNYRDYww5os1dCTPfjnLqZwwrQxlNYB1+TiZ+rj7PSPd8P+TdD5tQnx8ffSbOn1GuaFsFWY1T/huFN1UG9IHlYtWdTcKFBkAe23aDgfdvxfMjqayjeoHJJqEOzJaytoytoYILD47M2L5n8AXpQfw/KOQi1Amvl2NzkwogTm1OQvANRaCQazS7gSjdDVhnz7QUrl06RX6b+X8cpkGBAKPYSh3G/f0SlgXvGRPHW4nZtky4HENcoQSpQ/cY+5Nhuq6/WdM6QMx2T9A8zukrh6LTNTxI8yw9EjvU43/2ofwp2yodbxKZ2WoszG/rscoEsBrnDuILkOBxd/tkSoYjc8fR8giGhqeYXRYchnTM54tqUzrzyHUIVfVhPpB8LOnuBiP436HcIEZmKXK/2+uvXZ8Aj6q49rmd6d+2cpk8WSWnD+cduU1m5cm5QDFxW44s0r8SWOPfcQ85FTLxhx0=',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSTM=1706284751; BIDUPSID=C117306D69C3E4BA008A25BB285CFF61; BAIDUID=B7F72B04A4AC4F87C74E337AC724C546:FG=1; BAIDUID_BFESS=B7F72B04A4AC4F87C74E337AC724C546:FG=1; H_PS_PSSID=40043_39996; ZFY=buvjvWr:A5pJSYcdGIsh2:Agz68HPe8p1BOB:B88lsz7Ss:C; PSINO=5; delPer=0; H_WISE_SIDS=40043_39996; __bid_n=18cb89f28523728c425b1d; BDUSS=UV4fnVhNHV2Z09jTHRsandjYXNBamNJNVRXRW8tLTNzMW9udDBSMGZGVWlpOXhsRUFBQUFBJCQAAAAAAAAAAAEAAADG8h9UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACL-tGUi~rRlR; BDUSS_BFESS=UV4fnVhNHV2Z09jTHRsandjYXNBamNJNVRXRW8tLTNzMW9udDBSMGZGVWlpOXhsRUFBQUFBJCQAAAAAAAAAAAEAAADG8h9UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACL-tGUi~rRlR; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1705500161,1706450163; RT="z=1&dm=baidu.com&si=92452f11-b0b3-4ea2-a6f3-b89a8acb7ac6&ss=lrywzoc1&sl=n&tt=6f6&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2i4dk&ul=2jghk&hd=2jgix"; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1706621472; APPGUIDE_10_6_9=1',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

params = {
    'from': 'en',
    'to': 'zh',
}

with open('./baidu.js', 'r') as fp:
    js_code = fp.read()

word = input('::: ')

js = execjs.compile(js_code)
ret = js.call('getSignAndTime', word)

data = {
    'from': 'en',
    'to': 'zh',
    'query': word,
    'transtype': 'translang',
    'simple_means_flag': '3',
    'sign': ret['sign'],
    'token': '1fd4e0c49d42c9e608fed3fd473952af',
    'domain': 'common',
    'ts': ret['ts'],
}

response = requests.post('https://fanyi.baidu.com/v2transapi', params=params, cookies=cookies, headers=headers,
                         data=data)
print(response.json())
