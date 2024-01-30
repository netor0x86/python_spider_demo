const crypto = require('crypto')

/**
 * 获取请求的参数
 */
function getRequestParam() {
    mysticTime = (new Date).getTime()

    result = {
        sign: crypto.createHash('md5')
            .update(`client=fanyideskweb&mysticTime=${mysticTime}&product=webfanyi&key=fsdsogkndfokasodnaso`)
            .digest('hex'),
        mysticTime: mysticTime
    }

    return JSON.stringify(result)
}

function y(e) {
    return crypto.createHash("md5").update(e).digest()
}

/**
 * 解密返回值
 */
function decryptResult(result) {
    aesKey = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
    aesIv = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"

    const a = Buffer.alloc(16, y(aesKey))
        , i = Buffer.alloc(16, y(aesIv))
        , r = crypto.createDecipheriv("aes-128-cbc", a, i)

    let s = r.update(result, "base64", "utf-8");
    return s += r.final("utf-8")
}