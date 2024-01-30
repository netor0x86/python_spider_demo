import requests
import json
import execjs


def getRequestParam():
    """
    获取请求的动态参数
    """
    with open('./youdao.js', 'r') as fp:
        js_code = fp.read()
    js_obj = execjs.compile(js_code)
    return js_obj.call('getRequestParam')


def decryptResult(result):
    """
    解密返回的结果
    """
    with open('./youdao.js', 'r') as fp:
        with open('./youdao.js', 'r') as fp:
            js_code = fp.read()
        js_obj = execjs.compile(js_code)
        return js_obj.call('decryptResult', result)


def getCookies():
    return {
        'OUTFOX_SEARCH_USER_ID_NCOO': '1789425178.6243317',
        'OUTFOX_SEARCH_USER_ID': '-1553911374@223.12.69.155',
    }


def getHeaders():
    return {
        'Referer': 'https://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }


def getData(word, sign, mysticTime):
    return {
        'i': word,
        'from': 'auto',
        'to': '',
        'dictResult': 'true',
        'keyid': 'webfanyi',
        'sign': sign,
        'client': 'fanyideskweb',
        'product': 'webfanyi',
        'appVersion': '1.0.0',
        'vendor': 'web',
        'pointParam': 'client,mysticTime,product',
        'mysticTime': mysticTime,
        'keyfrom': 'fanyi.web',
        'mid': '1',
        'screen': '1',
        'model': '1',
        'network': 'wifi',
        'abtest': '0',
        'yduuid': 'abcdefg',
    }


def main():
    # 获取动态请求参数
    request_param = json.loads(getRequestParam())
    # 输入翻译内容
    word = input('>>> ')
    response = requests.post('https://dict.youdao.com/webtranslate',
                             cookies=getCookies(),
                             headers=getHeaders(),
                             data=getData(word, request_param.get('sign'), request_param.get('mysticTime')))

    # 解密返回内容
    json_content = json.loads(decryptResult(response.text))
    # 输出翻译后的内容
    print('translate ===>>>', json_content.get('translateResult')[0][0].get('tgt'))


if __name__ == '__main__':
    main()
