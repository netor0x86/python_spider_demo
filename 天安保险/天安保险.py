from Crypto.Cipher import AES
import base64
from Crypto.Util.Padding import pad
import requests

cookies = {
    'JSESSIONID': 'D885CBF3E8EDEE9A52FDCB6787ED6DB9',
    'cookiesession1': '678B286CJKLMNOPQRSTUV0234567E848',
    'ISEE_DEVICE_ID_V2': '9fa6b2b97a686a6eda7c001287b3e9bd',
    'ISEE_BIZ': '1021005dvdn.pwBgmj15o6SdVQ9cQ0S.T',
    'ISEE_COUNT': '72',
    'ISEE_LAST_URL': 'https%3A//tianaw.95505.cn/tacpc/%23/home/others%3Fid%3D71',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'JSESSIONID=D885CBF3E8EDEE9A52FDCB6787ED6DB9; cookiesession1=678B286CJKLMNOPQRSTUV0234567E848; ISEE_DEVICE_ID_V2=9fa6b2b97a686a6eda7c001287b3e9bd; ISEE_BIZ=1021005dvdn.pwBgmj15o6SdVQ9cQ0S.T; ISEE_COUNT=72; ISEE_LAST_URL=https%3A//tianaw.95505.cn/tacpc/%23/home/others%3Fid%3D71',
    'Origin': 'https://tianaw.95505.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://tianaw.95505.cn/tacpc/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'key': 'cxcRGyzCVrg6YblXiWGswx5tG0vxFKOX3V+GW9/7E7hx0NrfFJnzFPTt1ivHczuO/sHh6irn8unVN6hhVQSpB/rdnI7ClVAzHEE6h2h0W+YpOlc+fzLzQHY6jMkxn1a6kWM1CiW5jCyHlr3ziEeuQhbmwRxcrn6rAAPp9v1Kw/t2NBrk6OtRO5QnYFVJ88+PXVPUNwZIWR4m4C7F24e+4e+bk6Ur0D9zUeVxBz3dCxwsA3AhI6kZv8U8A+xiDmEJA6sOyrR2vqHAGqVDdNMC7JcrImXxOscuYWrAzRH4JiacGNzb/XbM0dI3VTiaA49Ir3XmbzMf46A20uZcoD8jGQ==',
    'keys': 'lA+2hLTl0C6Fzeq2i5robpS4vXLHp04r0D2WgO/nBgLSwfCZC0YbroGh/yoaVA3ca1nWZ1eX7r/l/a7ujzPmXI2UtvtVnSLg2Xsz0D2GGp8=',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

key = 'wjSr7JQzQ5rxeJ6Y'

data = '{"body":{"pageNo":1,"pageSize":4,"sold":"sold","commodityComClass":""},"head":{"userCode":null,"channelCode":"101","transTime":1715314279553,"transToken":"","customerId":null,"transSerialNumber":""}}'

aes = AES.new(key.encode(), AES.MODE_CBC, key.encode())
jsonkey = base64.b64encode(aes.encrypt(pad(data.encode(), 16)))
# print(jsonkey.decode())

params = {
    # 'jsonKey': 'n4kfX+i2tI4Xm94OOf4NzLMttc2YGh3YUaWCtWA2VstD1LFmKORoE5wDuQOwXk/JMjgYbwG7H8Fwn1ou4B7Zpqoi3A2WHYSOG14J1woh2qYWWHWbHIOaYspBBC1dyZMELGd9OIdfT/gNaNXkb/e61lKnmlmSinpoZcLinTBYinpwCtpaRTvQsW2zTm9VbsQQhwiGHiyy4voRmtgyduv1Q9X0oFqGHVx9VoZ3/AV6+95A6zD5dGdor0Kc/E9tEFigWtYFmaBDgmlo9Txfuj4A7A==',
    'jsonKey': jsonkey.decode()
}

json_data = {
    # 'jsonKey': 'n4kfX+i2tI4Xm94OOf4NzLMttc2YGh3YUaWCtWA2VstD1LFmKORoE5wDuQOwXk/JMjgYbwG7H8Fwn1ou4B7Zpqoi3A2WHYSOG14J1woh2qYWWHWbHIOaYspBBC1dyZMELGd9OIdfT/gNaNXkb/e61lKnmlmSinpoZcLinTBYinpwCtpaRTvQsW2zTm9VbsQQhwiGHiyy4voRmtgyduv1Q9X0oFqGHVx9VoZ3/AV6+95A6zD5dGdor0Kc/E9tEFigWtYFmaBDgmlo9Txfuj4A7A==',
    'jsonKey': jsonkey.decode()
}

response = requests.post(
    'https://tianaw.95505.cn/tacpc/tiananapp/marketing_product_commodity/commodityList',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
# print(response.json()['returns']['encryctReturns'])

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{"jsonKey":"n4kfX+i2tI4Xm94OOf4NzLMttc2YGh3YUaWCtWA2VstD1LFmKORoE5wDuQOwXk/JMjgYbwG7H8Fwn1ou4B7Zpqoi3A2WHYSOG14J1woh2qYWWHWbHIOaYspBBC1dyZMELGd9OIdfT/gNaNXkb/e61lKnmlmSinpoZcLinTBYinpwCtpaRTvQsW2zTm9VbsQQhwiGHiyy4voRmtgyduv1Q9X0oFqGHVx9VoZ3/AV6+95A6zD5dGdor0Kc/E9tEFigWtYFmaBDgmlo9Txfuj4A7A=="}'
# response = requests.post(
#    'https://tianaw.95505.cn/tacpc/tiananapp/marketing_product_commodity/commodityList',
#    params=params,
#    cookies=cookies,
#    headers=headers,
#    data=data,
# )
aes = AES.new(key.encode(), AES.MODE_CBC, key.encode())
dec = aes.decrypt(base64.b64decode(response.json()['returns']['encryctReturns']))
print(dec.decode())
