import requests
import hashlib
import time
from Crypto.Cipher import AES
import base64
from Crypto.Util.Padding import pad, unpad
import json

secretKey = "fsdsogkndfokasodnaso"
aesKey = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
aesIv = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"


def getMd5Digest(content):
    """
    返回key、iv的md5值，用于解密
    """
    md5 = hashlib.md5()
    md5.update(content.encode())
    return md5.digest()


def getDecryptContent(content):
    '''
    解密返回值
    '''
    # base64 解密啊
    decode_content = base64.b64decode(content.encode(), altchars='-_')

    # 获得 aes 的 key 和 iv
    key = getMd5Digest(aesKey)
    iv = getMd5Digest(aesIv)

    # aes 解密
    aes = AES.new(key, AES.MODE_CBC, iv)
    decrypt_content = aes.decrypt(decode_content)
    decrypt_content = unpad(decrypt_content, 16)

    return decrypt_content.decode()


def getMysticTime():
    """
    获取时间戳
    """
    return str(int(time.time() * 1000))


def getSign(mysticTime):
    """
    获取sign值
    """
    e = f'client=fanyideskweb&mysticTime={mysticTime}&product=webfanyi&key=fsdsogkndfokasodnaso'
    md5 = hashlib.md5()
    md5.update(e.encode())
    return md5.hexdigest()


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
    word = input('>>> ')
    mysticTime = getMysticTime()
    sign = getSign(mysticTime)
    response = requests.post('https://dict.youdao.com/webtranslate',
                             cookies=getCookies(),
                             headers=getHeaders(),
                             data=getData(word, sign, mysticTime))

    json_content = json.loads(getDecryptContent(response.text))
    print('translate ===>>>', json_content.get('translateResult')[0][0].get('tgt'))


if __name__ == '__main__':
    main()
