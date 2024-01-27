import requests
import execjs
import os


def get_token():
    ret = js.call('get_m_value')
    ret = ret.replace('丨', "%E4%B8%A8")
    return ret


headers = {
    'Referer':
        'https://match.yuanrenxue.cn/match/1',
    'Cookie': '',
    'User-Agent':
        '',
    'X-Requested-With':
        'XMLHttpRequest',
    'Accept':
        'application/json, text/javascript, */*; q=0.01'
}

js_path = os.getcwd() + '/match1.js'

with open(js_path, 'r') as p:
    js_code = p.read()
js = execjs.compile(js_code)

sum = 0
count = 0

for page in range(1, 6):
    token = get_token()
    url = f'https://match.yuanrenxue.cn/api/match/1?page={page}&m={token}'
    print('downloading page:::', page)

    for value in requests.get(url, headers=headers).json()['data']:
        sum += value['value']
        count += 1

print('target avg number ==>>', sum // count)
