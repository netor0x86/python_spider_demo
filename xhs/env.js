window = global;

delete global;
delete Buffer;

window.CanvasRenderingContext2D = {}
window.HTMLCanvasElement = {}
window.devicePixelRatio = 2
window.AudioContext = {}

// 补充 document 对象
document = {
    createElement: function (ele) {
        console.log('ele:::', ele)
        return {
            getContext: function () {
            }
        }
    },
    documentElement: function () {
    },
    cookie: 'abRequestId=20a5f287-8aca-5bab-9fdf-45cfb94cff09; a1=18aa656343584vnxom74uo55f3zeucvkcemzlytdy30000269770; webId=5764d58efe63dd43d91b4b0795425628; gid=yY00K2KqjjSjyY00K2Kq4dv9q2Y4hICl6W476fvl22iquuq8d7ShT1888JKjWW88iYSifdfS; xsecappid=xhs-pc-web; webBuild=4.16.0; unread={%22ub%22:%2266442062000000001e020fd3%22%2C%22ue%22:%2266246f60000000001c00959c%22%2C%22uc%22:25}; websectiga=634d3ad75ffb42a2ade2c5e1705a73c845837578aeb31ba0e442d75c648da36a; sec_poison_id=42fcfced-184e-41a1-b706-6737fde7e651'
}

navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    webdriver: false,
    platform: 'MacIntel',
    product: "Gecko",
    productSub: "20030107",
    geolocation: {},
    language: "zh-CN",
    languages: {0: "zh-CN", 1: "zh"},
    cookieEnabled: true,

}

location = {
    "ancestorOrigins": {},
    "href": "https://www.xiaohongshu.com/explore",
    "origin": "https://www.xiaohongshu.com",
    "protocol": "https:",
    "host": "www.xiaohongshu.com",
    "hostname": "www.xiaohongshu.com",
    "port": "",
    "pathname": "/explore",
    "search": "?channel_id=homefeed.food_v3",
    "hash": ""
}

screen = {}

external = {}

localStorage = {
    getItem: function () {
    }
}
