import requests
import execjs

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://music.163.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://music.163.com/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

params = {
    'csrf_token': '',
}

with open('01有道云音乐.js', 'r') as fp:
    js_code = fp.read()
js_engine = execjs.compile(js_code)
param = js_engine.call('getParam', '1415732182')
data = {
    # 'params': 'k6SnReoMNFLVq3gkbrGTfzASJkY2J04P6HyuDefxombF5xXSwxNWE0lWKyJCUPKaUlqR64Hu+V2SJMd9oK+DHKu8KzPUw58iB5XQIefOR0ZIHbNBy7gqhG8TARg14UdzUOv/rcq5fAUya/0MjYGBYw==',
    # 'encSecKey': '9b538b04b667cf84323e960895b1b7d6e2dbd5aa8ed03b25f8fb92eef52865891694bea1deff5d5013e63408bbb2186d6d99eb6301dfbe17344861e953eb4ab4811ed1379c889d8b51a0a3c57f3943db4ec8384af683f410751ab7f3edf04fbedbacc8b6fd0ba0e015ffe47e90db7af2a8f7a78816b73a4c0a065831ea9e87ea',
    'params': param['encText'],
    'encSecKey': param['encSecKey']
}

response = requests.post(
    'https://music.163.com/weapi/song/enhance/player/url/v1',
    params=params,
    headers=headers,
    data=data,
)
print(response.text)

response_json = response.json()
print(response_json['data'][0]['url'])

m4a_response = requests.get(response_json['data'][0]['url'])
with open('music.m4a', 'wb') as fp:
    fp.write(m4a_response.content)
