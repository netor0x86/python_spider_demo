import requests
import execjs

headers = {
    'Cookie':
        '',
    'Referer':
        'https://match.yuanrenxue.cn/match/3',
    'Accept':
        '*/*',
    'User-Agent':
        '',
}

sum = 0

for page in range(1, 6):
    func = "function m(){return btoa('yuanrenxue" + str(page) + "')}"

    js = execjs.compile(func)
    ret = js.call('m')

    session = requests.session()
    real_url = f'https://match.yuanrenxue.cn/api/match/12?page={page}&m=' + ret

    result1 = session.get(url=real_url, headers=headers)
    for keySet in result1.json().get('data'):
        sum += keySet.get('value')

print('target sum number ==>>', sum)
