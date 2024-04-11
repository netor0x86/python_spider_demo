const crypto = require('crypto-js');

function e(e, a) {
    return e = crypto.enc.Utf8.parse(e),
        a = crypto.enc.Utf8.parse(a),
        crypto.AES.encrypt(a, e, {
            mode: crypto.mode.CBC,
            padding: crypto.pad.Pkcs7,
            iv: e
        }).toString()
}

function k(e) {
    var a = '55b3b62613aef1a029bd7231109e051d'
    return a = 0 == e ? a.substring(0, 16) : a.substring(16, 32)
}

function aes_encrypt(data) {
    return e(k(0), data)
}

function encrypt(data) {
    var a = data;
    return void 0 == a ? a = {
        expire: (new Date).getTime()
    } : a.expire = (new Date).getTime(),
        data = aes_encrypt(JSON.stringify(a))
}

function get_encrypt(page) {
    data = {
        Type: 0,
        expire: (new Date).getTime(),
        page: page,
    }
    return encrypt(data)
}

function d(e, a) {
    e = crypto.enc.Utf8.parse(e);
    var l = crypto.AES.decrypt(a, e, {
        mode: crypto.mode.CBC,
        padding: crypto.pad.Pkcs7,
        iv: e
    });
    return crypto.enc.Utf8.stringify(l).toString()
}

function aes_decrypt(e) {
    var a = k(0).split("").reverse().join("");
    return d(a, e)
}
