import requests
import execjs

cookies = {
    '_ga': 'GA1.2.1497752407.1713311009',
    '_gat': '1',
    'auth_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU4MjY3NjEwLCJleHAiOjE3MTUxMjM3MTUsImV4cF92MiI6MTcxNTEyMzcxNSwiZGV2aWNlIjoiIiwidXNlcm5hbWUiOiJQaG9uZV84NjNhNDI4ZmIzZjkyODkxIiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiI0ZTc4ZWIzYTA0ZWIxMWVmYjJjNGJlNDJlMGYyOTcwOSJ9.e9Q9BCDrx9MKVNF02o3W6UV9wO3hxXM0tzi4X4NryHQ',
    'csrftoken': '06a349dac648ff3d2189e1d7b3b8d521',
    'tfstk': 'fZxsnuwfzIKeQj9CiNHFAV_rmySXfCiPk-6vEKEaHGITMoOfTlRqSK7fcd5eb1JNXSEXG6DMbfjaDE9ltt8wbF5AHQJVWiSwbmTfjH8a01lGcKdPcblr40JMIgjxabPwwHXd2O6YXS5YJ9KdI5yx40JMBdBBNdornHZ0ys1ADNQtvDChesIA6PHC9t6uk5dADv9dttzYMlEO9MBfEohMX86j51vsgS60273jFd1QDuwlsNn2Crr82H615C9OORw6AO_1wwW4AWKWedKlhnD8ls9yWCWHG0GC2UABcad-TkOcPEKNvhhK2wbvkU7X85HdDZK6XMTEq81pfKtCSeyz0dQWzUQBm0qMCafOA9xqtlCXJEKNSiVtGsxBphBXmjmBwg534_11TrwCro6CavMQor-Z2vGAEjz_BNBhCwkId5LcW9XBIvMQur7OK9-IdvazK',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22fyfglz%22%2C%22%24device_id%22%3A%2218ee94b44939ff-005554abc663f4-1c525637-2073600-18ee94b4494f69%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%2C%22first_id%22%3A%2218ee94b44939ff-005554abc663f4-1c525637-2073600-18ee94b4494f69%22%7D',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '_ga=GA1.2.1497752407.1713311009; _gat=1; auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU4MjY3NjEwLCJleHAiOjE3MTUxMjM3MTUsImV4cF92MiI6MTcxNTEyMzcxNSwiZGV2aWNlIjoiIiwidXNlcm5hbWUiOiJQaG9uZV84NjNhNDI4ZmIzZjkyODkxIiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiI0ZTc4ZWIzYTA0ZWIxMWVmYjJjNGJlNDJlMGYyOTcwOSJ9.e9Q9BCDrx9MKVNF02o3W6UV9wO3hxXM0tzi4X4NryHQ; csrftoken=06a349dac648ff3d2189e1d7b3b8d521; tfstk=fZxsnuwfzIKeQj9CiNHFAV_rmySXfCiPk-6vEKEaHGITMoOfTlRqSK7fcd5eb1JNXSEXG6DMbfjaDE9ltt8wbF5AHQJVWiSwbmTfjH8a01lGcKdPcblr40JMIgjxabPwwHXd2O6YXS5YJ9KdI5yx40JMBdBBNdornHZ0ys1ADNQtvDChesIA6PHC9t6uk5dADv9dttzYMlEO9MBfEohMX86j51vsgS60273jFd1QDuwlsNn2Crr82H615C9OORw6AO_1wwW4AWKWedKlhnD8ls9yWCWHG0GC2UABcad-TkOcPEKNvhhK2wbvkU7X85HdDZK6XMTEq81pfKtCSeyz0dQWzUQBm0qMCafOA9xqtlCXJEKNSiVtGsxBphBXmjmBwg534_11TrwCro6CavMQor-Z2vGAEjz_BNBhCwkId5LcW9XBIvMQur7OK9-IdvazK; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22fyfglz%22%2C%22%24device_id%22%3A%2218ee94b44939ff-005554abc663f4-1c525637-2073600-18ee94b4494f69%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%2C%22first_id%22%3A%2218ee94b44939ff-005554abc663f4-1c525637-2073600-18ee94b4494f69%22%7D',
    'origin': 'https://web.shanbay.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://web.shanbay.com/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-csrftoken': '06a349dac648ff3d2189e1d7b3b8d521',
}

params = {
    'ipp': '10',
    'page': '1',
    'type_of': 'NEW',
}

response = requests.get(
    'https://apiv3.shanbay.com/wordsapp/user_material_books/hpdru/learning/words/today_learning_items',
    params=params,
    cookies=cookies,
    headers=headers,
)

with open('./扇贝.js', 'r') as fp:
    js_code = fp.read()

js_engine = execjs.compile(js_code)
result = js_engine.call('get_decode', response.json()['data'])
print(result)
