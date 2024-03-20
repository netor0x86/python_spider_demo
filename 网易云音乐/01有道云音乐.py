import requests
import execjs

with open('01有道云音乐.js', 'r') as fp:
    js_code = fp.read()

js = execjs.compile(js_code)
ret = js.call('call')

url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
headers = {}
data = {
    'encSecKey': ret['encSecKey'],
}

response = requests.post(url, headers=headers, data=data)

response_json = response.json()
print(response_json['data'][0]['url'])

m4a_response = requests.get(response_json['data'][0]['url'])
with open('music.m4a', 'wb') as fp:
    fp.write(m4a_response.content)
