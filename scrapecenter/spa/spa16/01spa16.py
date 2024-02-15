import httpx

'''
使用 httpx 访问 http2.0 的网站
'''

client = httpx.Client(http2=True)
response = client.get('https://spa16.scrape.center/')
print(response.text)
client.close()

with httpx.Client(http2=True) as client:
    response = client.get('https://spa16.scrape.center/')
    print(response.text)
