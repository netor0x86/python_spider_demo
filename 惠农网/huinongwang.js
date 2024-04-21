require('./env')
require('./loader')
require('./module1')


// console.log(window.loader)
// console.log(window.loader(331))
// console.log(window.loader(511))
// console.log(window.loader2)
window.loader(331)
window.loader(511)
t = {
    $env: {
        UA:
            "mozilla/5.0 (macintosh; intel mac os x 10_15_7) applewebkit/537.36 (khtml, like gecko) chrome/124.0.0.0 safari/537.36",
        barHeight:
            90,
        inApp:
            false,
        inAppAndroid:
            false,
        inAppIOS:
            false,
        inBrowser:
            true,
        inDesktop:
            true,
        inWeex:
            false,
        isAndroid:
            false,
        isChrome:
            true,
        isEdge:
            false,
        isIE:
            false,
        isIE9:
            false,
        isIOS:
            false,
        isPhantomJS:
            false,
        weexPlatform:
            false,
    },
    env: {
        UA:
            "mozilla/5.0 (macintosh; intel mac os x 10_15_7) applewebkit/537.36 (khtml, like gecko) chrome/124.0.0.0 safari/537.36",
        barHeight:
            90,
        inApp:
            false,
        inAppAndroid:
            false,
        inAppIOS:
            false,
        inBrowser:
            true,
        inDesktop:
            true,
        inWeex:
            false,
        isAndroid:
            false,
        isChrome:
            true,
        isEdge:
            false,
        isIE:
            false,
        isIE9:
            false,
        isIOS:
            false,
        isPhantomJS:
            false,
        weexPlatform:
            false,
    },
    config: {
        banana:
            "https://gateway.cnhnb.com/banana",
        env:
            "pro",
        fontEnd:
            "https://m.cnhnb.com",
        m:
            "https://m.cnhnb.com",
        mobile:
            "https://mobile.cnhnb.com",
        monk:
            "https://gateway.cnhnb.com/monk",
        openapi:
            "https://openapi.cnhnb.com",
        peach:
            "",
        pigsy:
            "https://appapi.cnhnb.com",
    }
}
head = {
    'X-B3-TRACEID':
        "0LV9AG1GWLZ0HEI0",
    'X-CLIENT-APPID':
        5,
    'X-CLIENT-ENVIRONMENT':
        "pro",
    'X-CLIENT-ID':
        "10bc3b4-d6a3-4ac3-8bd0-e10ca1b7a",
    'X-CLIENT-NONCE':
        "03a453ad9a2389f32eb9277790453984",
    'X-CLIENT-PAGE':
        "/",
    'X-CLIENT-SID':
        "S_0LV9AG0Q773BH76D",
    'X-CLIENT-TICKET':
    undefined,
    'X-CLIENT-TIME':
        1713689438576,
    'X-CLIENT-UA': undefined,
    'X-HN-JOB':
        "If you see these message, I hope you dont hack us, I hope you can join us! Please visit https://www.cnhnkj.com/job.html",
}

// console.log(window.loader2(window.loader(311)).default(t, head))
function get_sign(time, nonce, trace_id) {
// function get_sign() {
    head['X-CLIENT-TIME'] = time
    head['X-CLIENT-NONCE'] = nonce
    head['X-B3-TRACEID'] = trace_id

    f = window.loader2(window.loader(311)).default(t, head)
    return f['X-CLIENT-SIGN'].toString()
}

// console.log(get_sign())

// header = window.loader2(window.loader(311)).default(t, head)
// console.log('--------------')
// console.log(header['X-CLIENT-SIGN'].toString())
// console.log(header['X-CLIENT-SIGN'].toString().length)

function get_nonce() {
    let t = true
    var e = (new Date).getTime();
    return (t ? "xxxxxxxxxxxxxyxxxxyxxxxxxxxxxxxx" : "xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxx").replace(/[xy]/g, (function (t) {
            var n = (e + 16 * Math.random()) % 16 | 0;
            return e = Math.floor(e / 16),
                ("x" == t ? n : 3 & n | 8).toString(16)
        }
    ))
}

function get_time() {
    return new Date().getTime().toString()
}


// console.log('2:', get_nonce())
// console.log('3:', get_time())


function Base36(t) {
    var r = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    for (var e = 9, b = t, n = ""; 0 != b;) {
        var o = b % 36
            , c = b / 36;
        n = r.charAt(o) + n,
            b = Math.round(Math.floor(c))
    }
    return ("0000000000000000" + n).substr(-e)
}

function randomInt(t, e) {
    return Math.floor(Math.random() * (e - t + 1) + t)
}

function get_trace_id() {
    return Base36(new Date().getTime(), 9) + Base36(randomInt(0, 78364164095), 7)
}

// console.log('1:', Base36(new Date().getTime(), 9) + Base36(randomInt(0, 78364164095), 7))


