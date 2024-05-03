/**
 * comParam_curTime
 * comParam_seqCode
 * comParam_signature
 * password
 */
const CryptoJS = require('crypto-js')

function get_com_param_cur_time() {
    return ((new Date).getTime() + 124).toString()
}

function get_com_param_seq_code() {
    var e, n, t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 32,
        r = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : 16,
        a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".split(""), o = [];
    if (r = r || a.length,
        t)
        for (e = 0; e < t; e++)
            o[e] = a[0 | Math.random() * r];
    else
        for (o[8] = o[13] = o[18] = o[23] = "-",
                 o[14] = "4",
                 e = 0; e < 36; e++)
            o[e] || (n = 0 | 16 * Math.random(),
                o[e] = a[19 === e ? 3 & n | 8 : n]);
    return o.join("")
}

// console.log(get_com_param_cur_time())
// console.log(get_com_param_seq_code())

function get_com_param_signature(n, r) {
    // n = 1714746766671;
    t = "s54zv9bm1vd5czfujy6nnuxj1l4g2ny6";
    // r = 'B25FED9E01E243CCC304188688352121';
    // console.log(CryptoJS.MD5(n + r + CryptoJS.MD5(r + t + n)).toString())
    return (CryptoJS.MD5(n + r + CryptoJS.MD5(r + t + n)).toString())
}

function _(e) {
    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {};
    if (e && "string" === typeof e) {
        var t = n.text || "0"
            , r = n.length || 24;
        if (e.length < r)
            for (var a = e.length; a < r; a++)
                e += t;
        else
            e = e.substring(0, r);
        return e
    }
}

function get_password(password, username) {
    // password = '12345asdf'
    username = _(username)

    key = CryptoJS.enc.Utf8.parse(username)

    cfg = {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    }
    var ciphertext = CryptoJS.TripleDES.encrypt(password, key, cfg);

    return ciphertext.toString()
}

