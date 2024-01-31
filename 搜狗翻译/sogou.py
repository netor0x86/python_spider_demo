import requests
import hashlib


def getCookie():
    return {
        'ABTEST': '0|1706618489|v17',
        'SNUID': 'D65B68BC6365744A70ABA33C64DDE2A7',
        'SUID': 'B23F0CDF8486A20A0000000065B8EE79',
        'wuid': '1706618489127',
        'FQV': '0f4b84ddbd787d0fc1588cc83f439033',
        'translate.sess': 'ce3416cf-d601-4939-a079-d77f75a9ee88',
        'SUV': '1706618489233',
        'SGINPUT_UPSCREEN': '1706618489256',
    }


def getHeaders():
    return {
        'Referer': 'https://fanyi.sogou.com/text?keyword=apple&transfrom=auto&transto=zh-CHS&model=general',
        'User-Agent': '',
    }


def getSign(word):
    d = f'autozh-CHS{word}109984457'

    md5 = hashlib.md5()
    md5.update(d.encode())

    return md5.hexdigest()


word = input('::: ')
sign = getSign(word)

json_data = {
    'from': 'auto',
    'to': 'zh-CHS',
    'text': word,
    'client': 'pc',
    'fr': 'browser_pc',
    'needQc': 1,
    's': sign,
    'uuid': 'dc28d715-c96a-490f-9ed2-6140e3433451',
    'exchange': False,
}


def getUrl():
    return 'https://fanyi.sogou.com/api/transpc/text/result'


def getTranslate(response):
    translate = response.json()
    return translate['data']['translate']['dit']


def main():
    response = requests.post(getUrl(),
                             cookies=getCookie(),
                             headers=getHeaders(),
                             json=json_data)

    print('translate ===>>>', getTranslate(response))


if __name__ == '__main__':
    main()
