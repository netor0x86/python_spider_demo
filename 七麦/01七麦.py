import requests
import execjs

with open('01七麦.js', 'r') as fp:
    js_code = fp.read()

url = 'https://api.qimai.cn/indexV2/getIndexRank'
params = {
    'setting': 0,
    'genre': 6014
}

js = execjs.compile(js_code)
analysis = js.call('get_analysis', url, params)
print(analysis)
params['analysis'] = analysis

resp = requests.get(url, params, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
})

print(resp.json())
