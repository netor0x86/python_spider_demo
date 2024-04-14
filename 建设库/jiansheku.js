const crypto = require('crypto')

function Mu(t) {
    return crypto.createHash('md5').update(t).digest('hex')
}

function Su(e, t, time) {
    var n = t + e + time;
    return n = Mu(n)
}

function Cu(e) {
    var t = Ou(e)
        , n = "";
    for (var i in t) {
        var r = ku(e[t[i]]);
        null != r && "" != r.toString() && (n += t[i] + "=" + r + "&")
    }
    return n
}

function ku(t) {
    var n;
    if (Array.isArray(t)) {
        for (var r in n = new Array,
            t) {
            var o = t[r];
            for (var i in o)
                null == o[i] ? delete t[r][i] : Array.isArray(t[r][i]) && e(t[r][i])
        }
        return n = t,
            JSON.stringify(n).replace(/^(\s|")+|(\s|")+$/g, "")
    }
    return n = t && t.constructor === Object ? JSON.stringify(t) : t
}

function Ou(e) {
    var t = new Array
        , n = 0;
    for (var i in e)
        t[n] = i,
            n++;
    return t.sort()
}

function get_sign(data) {

    f = (new Date).getTime()
    time = f

    // t = 'achievementQueryDto=[]&achievementQueryType=and&aptitudeQueryDto={"queryType":"and","nameStr":"","aptitudeQueryType":"and","businessScopeQueryType":"or","filePlaceType":"1","aptitudeDtoList":[{"codeStr":"","queryType":"and","aptitudeType":"qualification"}],"aptitudeSource":"new"}&page={"page":1,"limit":20,"field":"","order":""}&personnelQueryDto={"queryType":"and"}&'
    t = Cu(data)
    ret = Su("ghaepVf6IhcHmgnk4NCTXLApxQkBcvh1", Su("mwMlWOdyM7OXbjzQPulT1ndRZIAjShDB", Su("ZuSj0gwgsKXP4fTEz55oAG2q2p1SVGKK", t, time), time), time)
    return {time: f.toString(), sign: ret}
}

// console.log(ret)