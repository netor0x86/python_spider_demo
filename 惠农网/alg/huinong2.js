const CryptoJS = require('crypto-js')

window = global
delete global
delete Buffer

function cryptoMd5(data)
{
    const encrypted = CryptoJS.MD5(data)

    return encrypted.toString()
}

function cryptoSha1(data)
{
    const encrypted = CryptoJS.SHA1(data)

    return encrypted.toString()
}

function cryptoSha384(data)
{
    const encrypted = CryptoJS.SHA384(data)

    return encrypted.toString()
}
// ================SOURCE
!(function(t, e) {
    console.log('start')
    t.exports = r;
    var n = null;
    try {
        n = new WebAssembly.Instance(new WebAssembly.Module(new Uint8Array([0, 97, 115, 109, 1, 0, 0, 0, 1, 13, 2, 96, 0, 1, 127, 96, 4, 127, 127, 127, 127, 1, 127, 3, 7, 6, 0, 1, 1, 1, 1, 1, 6, 6, 1, 127, 1, 65, 0, 11, 7, 50, 6, 3, 109, 117, 108, 0, 1, 5, 100, 105, 118, 95, 115, 0, 2, 5, 100, 105, 118, 95, 117, 0, 3, 5, 114, 101, 109, 95, 115, 0, 4, 5, 114, 101, 109, 95, 117, 0, 5, 8, 103, 101, 116, 95, 104, 105, 103, 104, 0, 0, 10, 191, 1, 6, 4, 0, 35, 0, 11, 36, 1, 1, 126, 32, 0, 173, 32, 1, 173, 66, 32, 134, 132, 32, 2, 173, 32, 3, 173, 66, 32, 134, 132, 126, 34, 4, 66, 32, 135, 167, 36, 0, 32, 4, 167, 11, 36, 1, 1, 126, 32, 0, 173, 32, 1, 173, 66, 32, 134, 132, 32, 2, 173, 32, 3, 173, 66, 32, 134, 132, 127, 34, 4, 66, 32, 135, 167, 36, 0, 32, 4, 167, 11, 36, 1, 1, 126, 32, 0, 173, 32, 1, 173, 66, 32, 134, 132, 32, 2, 173, 32, 3, 173, 66, 32, 134, 132, 128, 34, 4, 66, 32, 135, 167, 36, 0, 32, 4, 167, 11, 36, 1, 1, 126, 32, 0, 173, 32, 1, 173, 66, 32, 134, 132, 32, 2, 173, 32, 3, 173, 66, 32, 134, 132, 129, 34, 4, 66, 32, 135, 167, 36, 0, 32, 4, 167, 11, 36, 1, 1, 126, 32, 0, 173, 32, 1, 173, 66, 32, 134, 132, 32, 2, 173, 32, 3, 173, 66, 32, 134, 132, 130, 34, 4, 66, 32, 135, 167, 36, 0, 32, 4, 167, 11])),{}).exports
    } catch (t) {}
    function r(t, e, n) {
        this.low = 0 | t,
        this.high = 0 | e,
        this.unsigned = !!n
    }
    function o(t) {
        return !0 === (t && t.__isLong__)
    }
    r.prototype.__isLong__,
    Object.defineProperty(r.prototype, "__isLong__", {
        value: !0
    }),
    r.isLong = o;
    var c = {}
      , f = {};
    function l(t, e) {
        var n, r, o;
        return e ? (o = 0 <= (t >>>= 0) && t < 256) && (r = f[t]) ? r : (n = d(t, (0 | t) < 0 ? -1 : 0, !0),
        o && (f[t] = n),
        n) : (o = -128 <= (t |= 0) && t < 128) && (r = c[t]) ? r : (n = d(t, t < 0 ? -1 : 0, !1),
        o && (c[t] = n),
        n)
    }
    function h(t, e) {
        if (isNaN(t))
            return e ? k : x;
        if (e) {
            if (t < 0)
                return k;
            if (t >= _)
                return R
        } else {
            if (t <= -M)
                return j;
            if (t + 1 >= M)
                return A
        }
        return t < 0 ? h(-t, e).neg() : d(t % w | 0, t / w | 0, e)
    }
    function d(t, e, n) {
        return new r(t,e,n)
    }
    r.fromInt = l,
    r.fromNumber = h,
    r.fromBits = d;
    var m = Math.pow;
    function v(t, e, n) {
        if (0 === t.length)
            throw Error("empty string");
        if ("NaN" === t || "Infinity" === t || "+Infinity" === t || "-Infinity" === t)
            return x;
        if ("number" == typeof e ? (n = e,
        e = !1) : e = !!e,
        (n = n || 10) < 2 || 36 < n)
            throw RangeError("radix");
        var p;
        if ((p = t.indexOf("-")) > 0)
            throw Error("interior hyphen");
        if (0 === p)
            return v(t.substring(1), e, n).neg();
        for (var r = h(m(n, 8)), o = x, i = 0; i < t.length; i += 8) {
            var c = Math.min(8, t.length - i)
              , f = parseInt(t.substring(i, i + c), n);
            if (c < 8) {
                var l = h(m(n, c));
                o = o.mul(l).add(h(f))
            } else
                o = (o = o.mul(r)).add(h(f))
        }
        return o.unsigned = e,
        o
    }
    window.v = v
    function y(t, e) {
        return "number" == typeof t ? h(t, e) : "string" == typeof t ? v(t, e) : d(t.low, t.high, "boolean" == typeof e ? e : t.unsigned)
    }
    r.fromString = v,
    r.fromValue = y;
    var w = 4294967296
      , _ = w * w
      , M = _ / 2
      , S = l(1 << 24)
      , x = l(0);
    r.ZERO = x;
    var k = l(0, !0);
    r.UZERO = k;
    var E = l(1);
    r.ONE = E;
    var C = l(1, !0);
    r.UONE = C;
    var O = l(-1);
    r.NEG_ONE = O;
    var A = d(-1, 2147483647, !1);
    r.MAX_VALUE = A;
    var R = d(-1, -1, !0);
    r.MAX_UNSIGNED_VALUE = R;
    var j = d(0, -2147483648, !1);
    r.MIN_VALUE = j;
    var T = r.prototype;
    T.toInt = function() {
        return this.unsigned ? this.low >>> 0 : this.low
    }
    ,
    T.toNumber = function() {
        return this.unsigned ? (this.high >>> 0) * w + (this.low >>> 0) : this.high * w + (this.low >>> 0)
    }
    ,
    T.toString = function(t) {
        if ((t = t || 10) < 2 || 36 < t)
            throw RangeError("radix");
        if (this.isZero())
            return "0";
        if (this.isNegative()) {
            if (this.eq(j)) {
                var e = h(t)
                  , div = this.div(e)
                  , n = div.mul(e).sub(this);
                return div.toString(t) + n.toInt().toString(t)
            }
            return "-" + this.neg().toString(t)
        }
        for (var r = h(m(t, 6), this.unsigned), o = this, c = ""; ; ) {
            var f = o.div(r)
              , l = (o.sub(f.mul(r)).toInt() >>> 0).toString(t);
            if ((o = f).isZero())
                return l + c;
            for (; l.length < 6; )
                l = "0" + l;
            c = "" + l + c
        }
    }
    ,
    T.getHighBits = function() {
        return this.high
    }
    ,
    T.getHighBitsUnsigned = function() {
        return this.high >>> 0
    }
    ,
    T.getLowBits = function() {
        return this.low
    }
    ,
    T.getLowBitsUnsigned = function() {
        return this.low >>> 0
    }
    ,
    T.getNumBitsAbs = function() {
        if (this.isNegative())
            return this.eq(j) ? 64 : this.neg().getNumBitsAbs();
        for (var t = 0 != this.high ? this.high : this.low, e = 31; e > 0 && 0 == (t & 1 << e); e--)
            ;
        return 0 != this.high ? e + 33 : e + 1
    }
    ,
    T.isZero = function() {
        return 0 === this.high && 0 === this.low
    }
    ,
    T.eqz = T.isZero,
    T.isNegative = function() {
        return !this.unsigned && this.high < 0
    }
    ,
    T.isPositive = function() {
        return this.unsigned || this.high >= 0
    }
    ,
    T.isOdd = function() {
        return 1 == (1 & this.low)
    }
    ,
    T.isEven = function() {
        return 0 == (1 & this.low)
    }
    ,
    T.equals = function(t) {
        return o(t) || (t = y(t)),
        (this.unsigned === t.unsigned || this.high >>> 31 != 1 || t.high >>> 31 != 1) && (this.high === t.high && this.low === t.low)
    }
    ,
    T.eq = T.equals,
    T.notEquals = function(t) {
        return !this.eq(t)
    }
    ,
    T.neq = T.notEquals,
    T.ne = T.notEquals,
    T.lessThan = function(t) {
        return this.comp(t) < 0
    }
    ,
    T.lt = T.lessThan,
    T.lessThanOrEqual = function(t) {
        return this.comp(t) <= 0
    }
    ,
    T.lte = T.lessThanOrEqual,
    T.le = T.lessThanOrEqual,
    T.greaterThan = function(t) {
        return this.comp(t) > 0
    }
    ,
    T.gt = T.greaterThan,
    T.greaterThanOrEqual = function(t) {
        return this.comp(t) >= 0
    }
    ,
    T.gte = T.greaterThanOrEqual,
    T.ge = T.greaterThanOrEqual,
    T.compare = function(t) {
        if (o(t) || (t = y(t)),
        this.eq(t))
            return 0;
        var e = this.isNegative()
          , n = t.isNegative();
        return e && !n ? -1 : !e && n ? 1 : this.unsigned ? t.high >>> 0 > this.high >>> 0 || t.high === this.high && t.low >>> 0 > this.low >>> 0 ? -1 : 1 : this.sub(t).isNegative() ? -1 : 1
    }
    ,
    T.comp = T.compare,
    T.negate = function() {
        return !this.unsigned && this.eq(j) ? j : this.not().add(E)
    }
    ,
    T.neg = T.negate,
    T.add = function(t) {
        o(t) || (t = y(t));
        var e = this.high >>> 16
          , n = 65535 & this.high
          , r = this.low >>> 16
          , c = 65535 & this.low
          , f = t.high >>> 16
          , l = 65535 & t.high
          , h = t.low >>> 16
          , m = 0
          , v = 0
          , w = 0
          , _ = 0;
        return w += (_ += c + (65535 & t.low)) >>> 16,
        v += (w += r + h) >>> 16,
        m += (v += n + l) >>> 16,
        m += e + f,
        d((w &= 65535) << 16 | (_ &= 65535), (m &= 65535) << 16 | (v &= 65535), this.unsigned)
    }
    ,
    T.subtract = function(t) {
        return o(t) || (t = y(t)),
        this.add(t.neg())
    }
    ,
    T.sub = T.subtract,
    T.multiply = function(t) {
        if (this.isZero())
            return x;
        if (o(t) || (t = y(t)),
        n)
            return d(n.mul(this.low, this.high, t.low, t.high), n.get_high(), this.unsigned);
        if (t.isZero())
            return x;
        if (this.eq(j))
            return t.isOdd() ? j : x;
        if (t.eq(j))
            return this.isOdd() ? j : x;
        if (this.isNegative())
            return t.isNegative() ? this.neg().mul(t.neg()) : this.neg().mul(t).neg();
        if (t.isNegative())
            return this.mul(t.neg()).neg();
        if (this.lt(S) && t.lt(S))
            return h(this.toNumber() * t.toNumber(), this.unsigned);
        var e = this.high >>> 16
          , r = 65535 & this.high
          , c = this.low >>> 16
          , f = 65535 & this.low
          , l = t.high >>> 16
          , m = 65535 & t.high
          , v = t.low >>> 16
          , w = 65535 & t.low
          , _ = 0
          , M = 0
          , k = 0
          , E = 0;
        return k += (E += f * w) >>> 16,
        M += (k += c * w) >>> 16,
        k &= 65535,
        M += (k += f * v) >>> 16,
        _ += (M += r * w) >>> 16,
        M &= 65535,
        _ += (M += c * v) >>> 16,
        M &= 65535,
        _ += (M += f * m) >>> 16,
        _ += e * w + r * v + c * m + f * l,
        d((k &= 65535) << 16 | (E &= 65535), (_ &= 65535) << 16 | (M &= 65535), this.unsigned)
    }
    ,
    T.mul = T.multiply,
    T.divide = function(t) {
        if (o(t) || (t = y(t)),
        t.isZero())
            throw Error("division by zero");
        var e, r, c;
        if (n)
            return this.unsigned || -2147483648 !== this.high || -1 !== t.low || -1 !== t.high ? d((this.unsigned ? n.div_u : n.div_s)(this.low, this.high, t.low, t.high), n.get_high(), this.unsigned) : this;
        if (this.isZero())
            return this.unsigned ? k : x;
        if (this.unsigned) {
            if (t.unsigned || (t = t.toUnsigned()),
            t.gt(this))
                return k;
            if (t.gt(this.shru(1)))
                return C;
            c = k
        } else {
            if (this.eq(j))
                return t.eq(E) || t.eq(O) ? j : t.eq(j) ? E : (e = this.shr(1).div(t).shl(1)).eq(x) ? t.isNegative() ? E : O : (r = this.sub(t.mul(e)),
                c = e.add(r.div(t)));
            if (t.eq(j))
                return this.unsigned ? k : x;
            if (this.isNegative())
                return t.isNegative() ? this.neg().div(t.neg()) : this.neg().div(t).neg();
            if (t.isNegative())
                return this.div(t.neg()).neg();
            c = x
        }
        for (r = this; r.gte(t); ) {
            e = Math.max(1, Math.floor(r.toNumber() / t.toNumber()));
            for (var f = Math.ceil(Math.log(e) / Math.LN2), l = f <= 48 ? 1 : m(2, f - 48), v = h(e), w = v.mul(t); w.isNegative() || w.gt(r); )
                w = (v = h(e -= l, this.unsigned)).mul(t);
            v.isZero() && (v = E),
            c = c.add(v),
            r = r.sub(w)
        }
        return c
    }
    ,
    T.div = T.divide,
    T.modulo = function(t) {
        return o(t) || (t = y(t)),
        n ? d((this.unsigned ? n.rem_u : n.rem_s)(this.low, this.high, t.low, t.high), n.get_high(), this.unsigned) : this.sub(this.div(t).mul(t))
    }
    ,
    T.mod = T.modulo,
    T.rem = T.modulo,
    T.not = function() {
        return d(~this.low, ~this.high, this.unsigned)
    }
    ,
    T.and = function(t) {
        return o(t) || (t = y(t)),
        d(this.low & t.low, this.high & t.high, this.unsigned)
    }
    ,
    T.or = function(t) {
        return o(t) || (t = y(t)),
        d(this.low | t.low, this.high | t.high, this.unsigned)
    }
    ,
    T.xor = function(t) {
        return o(t) || (t = y(t)),
        d(this.low ^ t.low, this.high ^ t.high, this.unsigned)
    }
    ,
    T.shiftLeft = function(t) {
        return o(t) && (t = t.toInt()),
        0 == (t &= 63) ? this : t < 32 ? d(this.low << t, this.high << t | this.low >>> 32 - t, this.unsigned) : d(0, this.low << t - 32, this.unsigned)
    }
    ,
    T.shl = T.shiftLeft,
    T.shiftRight = function(t) {
        return o(t) && (t = t.toInt()),
        0 == (t &= 63) ? this : t < 32 ? d(this.low >>> t | this.high << 32 - t, this.high >> t, this.unsigned) : d(this.high >> t - 32, this.high >= 0 ? 0 : -1, this.unsigned)
    }
    ,
    T.shr = T.shiftRight,
    T.shiftRightUnsigned = function(t) {
        if (o(t) && (t = t.toInt()),
        0 === (t &= 63))
            return this;
        var e = this.high;
        return t < 32 ? d(this.low >>> t | e << 32 - t, e >>> t, this.unsigned) : d(32 === t ? e : e >>> t - 32, 0, this.unsigned)
    }
    ,
    T.shru = T.shiftRightUnsigned,
    T.shr_u = T.shiftRightUnsigned,
    T.toSigned = function() {
        return this.unsigned ? d(this.low, this.high, !1) : this
    }
    ,
    T.toUnsigned = function() {
        return this.unsigned ? this : d(this.low, this.high, !0)
    }
    ,
    T.toBytes = function(t) {
        return t ? this.toBytesLE() : this.toBytesBE()
    }
    ,
    T.toBytesLE = function() {
        var t = this.high
          , e = this.low;
        return [255 & e, e >>> 8 & 255, e >>> 16 & 255, e >>> 24, 255 & t, t >>> 8 & 255, t >>> 16 & 255, t >>> 24]
    }
    ,
    T.toBytesBE = function() {
        var t = this.high
          , e = this.low;
        return [t >>> 24, t >>> 16 & 255, t >>> 8 & 255, 255 & t, e >>> 24, e >>> 16 & 255, e >>> 8 & 255, 255 & e]
    }
    ,
    r.fromBytes = function(t, e, n) {
        return n ? r.fromBytesLE(t, e) : r.fromBytesBE(t, e)
    }
    ,
    r.fromBytesLE = function(t, e) {
        return new r(t[0] | t[1] << 8 | t[2] << 16 | t[3] << 24,t[4] | t[5] << 8 | t[6] << 16 | t[7] << 24,e)
    }
    ,
    r.fromBytesBE = function(t, e) {
        return new r(t[4] << 24 | t[5] << 16 | t[6] << 8 | t[7],t[0] << 24 | t[1] << 16 | t[2] << 8 | t[3],e)
    }
}({}, {}))
// ================API
function get_nonce(timestamp)
{
    function l(t) {
        var e = timestamp;
        return (t ? "xxxxxxxxxxxxxyxxxxyxxxxxxxxxxxxx" : "xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxx").replace(/[xy]/g, (function(t) {
            var n = (e + 16 * Math.random()) % 16 | 0;
            return e = Math.floor(e / 16),
            ("x" == t ? n : 3 & n | 8).toString(16)
        }
        ))
    }

    return l(!0)
}

function get_traceid(timestamp)
{
    function randomInt(t, e) {
        return Math.floor(Math.random() * (e - t + 1) + t)
    }

    var r = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    function o(t) {
        for (var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : 9, b = t, n = ""; 0 != b; ) {
            var o = b % 36
              , c = b / 36;
            n = r.charAt(o) + n,
            b = Math.round(Math.floor(c))
        }
        return ("0000000000000000" + n).substr(-e)
    }

    return o(timestamp, 9) + o(randomInt(0, 78364164095), 7)
}

function get_header() {
    let timestamp = new Date().getTime()

    head = {
        "X-CLIENT-APPID": "5",
        "X-CLIENT-PAGE": "/",
        "X-HN-JOB": "If you see these message, I hope you dont hack us, I hope you can join us! Please visit https://www.cnhnkj.com/job.html",
        "X-CLIENT-ID": "7f3531a-7a83-4e2a-9fb4-be9e9637f",
        "X-CLIENT-SID": "S_" + get_traceid(timestamp - 1000),
        "X-B3-TRACEID": get_traceid(timestamp),
        "X-CLIENT-TIME": timestamp.toString(),
        "X-CLIENT-NONCE": get_nonce(timestamp),
        "X-CLIENT-ENVIRONMENT": "pro",
    }

    K = {
        "nonce": head["X-CLIENT-NONCE"],
        "timestamp": head["X-CLIENT-TIME"],
        "deviceId": head["X-CLIENT-ID"],
        "secret": "EOi^0N5sWWHhkrF2A0gekY9U20BgnAcr",
        "secretType": 2
    }

    R = (d = K).nonce

    j = d.timestamp
    T = d.deviceId
    I = d.secret
    P = d.secretType
    m = R

    L = cryptoMd5(m)
    console.log("L:", L)

    y = j

    B = cryptoSha1(y)
    console.log("B:", B)

    _ = T
    M = R

    N = cryptoMd5(M + _)
    console.log("N:", N)

    x = I
    k = j
    C = ""

    C = cryptoSha1(x + k)
    console.log("C:", C)

    C = C.substring(C.length - 16, C.length - 1)
    console.log("C:", C)

    D = window.v(C, !0, 16)['toUnsigned']()['toString'](10)
    console.log("D:", D)

    A = [L, B, N, D]
    console.log("A:", A)

    F = A.reduce((function(t, e) {
        return t + "!" + e
    }))
    console.log('F:', F)

    sign = cryptoSha384(F)
    console.log('sign:', sign)

    head['X-CLIENT-SIGN'] = sign
    return head
}

console.log(get_header())