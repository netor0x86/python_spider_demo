crypto = require('crypto')

function s(t, e) {
    return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
}

function l(t) {
    for (var e = Object.keys(t).sort(s), n = "", a = 0; a < e.length; a++)
        if (void 0 !== t[e[a]])
            if (t[e[a]] && t[e[a]] instanceof Object || t[e[a]] instanceof Array) {
                var i = JSON.stringify(t[e[a]]);
                n += e[a] + i
            } else
                n += e[a] + t[e[a]];
    return n
}

var r = {
    a: "B3978D054A72A7002063637CCDF6B2E5"
}

function d(t) {
    for (var e in t)
        "" !== t[e] && void 0 !== t[e] || delete t[e];
    var n = r["a"] + l(t);
    return crypto.createHash("md5").update(n, "utf8").digest("hex").toLocaleLowerCase()
}

// console.log(d({"type": "53", "ts": 1715523449561}))