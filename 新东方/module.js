window = global;

(window.webpackJsonp_N_E = window.webpackJsonp_N_E || []).push([[6], {
    "/0+H": function(e, t, n) {
        "use strict";
        t.__esModule = !0,
        t.isInAmpMode = c,
        t.useAmp = function() {
            return c(o.default.useContext(a.AmpStateContext))
        }
        ;
        var r, o = (r = n("q1tI")) && r.__esModule ? r : {
            default: r
        }, a = n("lwAK");
        function c() {
            var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {}
              , t = e.ampFirst
              , n = void 0 !== t && t
              , r = e.hybrid
              , o = void 0 !== r && r
              , a = e.hasQuery
              , c = void 0 !== a && a;
            return n || o && c
        }
    },
    "20a2": function(e, t, n) {
        e.exports = n("nOHt")
    },
    "48fX": function(e, t, n) {
        var r = n("qhzo");
        e.exports = function(e, t) {
            if ("function" !== typeof t && null !== t)
                throw new TypeError("Super expression must either be null or a function");
            e.prototype = Object.create(t && t.prototype, {
                constructor: {
                    value: e,
                    writable: !0,
                    configurable: !0
                }
            }),
            t && r(e, t)
        }
    },
    "5M6V": function(e, t, n) {
        "use strict";
        var r = n("nKUr")
          , o = n("vJKn")
          , a = n.n(o)
          , c = n("rg98")
          , i = n("q1tI")
          , s = n("g4pe")
          , u = n.n(s)
          , d = n("qjqm")
          , l = (n("iFgM"),
        n("DTmv"));
        function f(e, t) {
            var n;
            if ("undefined" === typeof Symbol || null == e[Symbol.iterator]) {
                if (Array.isArray(e) || (n = function(e, t) {
                    if (!e)
                        return;
                    if ("string" === typeof e)
                        return p(e, t);
                    var n = Object.prototype.toString.call(e).slice(8, -1);
                    "Object" === n && e.constructor && (n = e.constructor.name);
                    if ("Map" === n || "Set" === n)
                        return Array.from(e);
                    if ("Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))
                        return p(e, t)
                }(e)) || t && e && "number" === typeof e.length) {
                    n && (e = n);
                    var r = 0
                      , o = function() {};
                    return {
                        s: o,
                        n: function() {
                            return r >= e.length ? {
                                done: !0
                            } : {
                                done: !1,
                                value: e[r++]
                            }
                        },
                        e: function(e) {
                            throw e
                        },
                        f: o
                    }
                }
                throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
            }
            var a, c = !0, i = !1;
            return {
                s: function() {
                    n = e[Symbol.iterator]()
                },
                n: function() {
                    var e = n.next();
                    return c = e.done,
                    e
                },
                e: function(e) {
                    i = !0,
                    a = e
                },
                f: function() {
                    try {
                        c || null == n.return || n.return()
                    } finally {
                        if (i)
                            throw a
                    }
                }
            }
        }
        function p(e, t) {
            (null == t || t > e.length) && (t = e.length);
            for (var n = 0, r = new Array(t); n < t; n++)
                r[n] = e[n];
            return r
        }
        var h = n("aCH8")
          , m = function(e) {
            var t = e.hotKeywordList
              , n = e.cityCode
              , o = e.telephone
              , s = e.cityList
              , u = e.getSerachClass
              , p = e.kw
              , m = e.isHiddenHeaderSearch
              , y = e.page
              , b = Object(i.useState)("")
              , v = b[0]
              , g = b[1]
              , w = Object(i.useState)(p || "")
              , j = w[0]
              , x = w[1]
              , O = Object(i.useState)("")
              , C = O[0]
              , k = O[1]
              , S = Object(i.useState)("")
              , _ = (S[0],
            S[1]);
            Object(i.useEffect)((function() {
                _("detail" == y ? "" : window.xdfCommonCitySelect.BUTTON_CLASS_NAME),
                window.xdfCommonCitySelect.init("pc"),
                window.xdfCommonCitySelect.onChange((function(e) {
                    var t = e.detail;
                    if (t.code != n) {
                        var r = []
                          , o = function() {
                            for (var e = ((arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : window.location.href).split("?")[1] || "").split("&"), t = {}, n = 0; n < e.length; n++) {
                                var r = e[n].split("=")
                                  , o = r[0];
                                o && (t[o] = r[1])
                            }
                            return t
                        }();
                        delete o.cid,
                        o.cityCode = t.code;
                        for (var a = 0, c = Object.keys(o); a < c.length; a++) {
                            var i = c[a];
                            r.push("".concat(i, "=").concat(o[i]))
                        }
                        var s = "".concat(window.location.origin).concat(window.location.pathname, "?").concat(r.join("&"));
                        window.location.replace(s)
                    }
                }
                )),
                n || "teacher-detail" == y || "detail" == y || window.xdfCommonCitySelect.open()
            }
            ), []),
            Object(i.useEffect)((function() {
                ("teacher-detail" != y && "detail" != y || n) && window.xdfCommonCitySelect.getAsync(n).then((function(e) {
                    n == e.code || "teacher-detail" == y ? (window.xdfCommonCitySelect.close(),
                    g(e.name),
                    Object(d.n)("soukecityid", e.code),
                    Object(d.n)("cityName", e.name)) : setTimeout((function() {
                        window.xdfCommonCitySelect.open()
                    }
                    ), 300)
                }
                )).catch((function(e) {
                    window.xdfCommonCitySelect.open()
                }
                ))
            }
            ), [n]);
            var A = function() {
                var e = Object(c.a)(a.a.mark((function e(t) {
                    var r, o, c, i, s, u;
                    return a.a.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (r = !1,
                                !/^[0-9a-zA-Z]*$/i.test(t)) {
                                    e.next = 11;
                                    break
                                }
                                return o = "appId=".concat(l.a, "&cityCode=").concat(n, "&t=").concat((new Date).getTime(), "&classCodes=").concat(t),
                                e.next = 6,
                                fetch("".concat(l.d, "/product/v1/class/list?").concat(o), {
                                    headers: {
                                        "Content-Type": "application/json",
                                        sign: h("".concat(o).concat(l.b))
                                    }
                                });
                            case 6:
                                return c = e.sent,
                                e.next = 9,
                                c.json();
                            case 9:
                                200 == (i = e.sent).code && i.data.length >= 1 && (s = i.data[0],
                                u = "/item/".concat(s.cityCode, "-").concat(s.schoolId, "-").concat(s.code, ".html"),
                                r = !0,
                                window.location.href = u);
                            case 11:
                                return e.next = 13,
                                r;
                            case 13:
                                return e.abrupt("return", e.sent);
                            case 14:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )));
                return function(t) {
                    return e.apply(this, arguments)
                }
            }()
              , I = function() {
                var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : j;
                e != j && x(e),
                A(e),
                window.location.pathname.indexOf("/search") >= 0 ? u && u(1, e, !0) : window.open("/search?searchResult=true&cityCode=".concat(n, "&kw=").concat(e))
            };
            return Object(i.useEffect)((function() {
                k(Object(d.e)("U2NickName")),
                j && A(j)
            }
            ), []),
            Object(r.jsxs)("div", {
                className: "header",
                children: [Object(r.jsx)("div", {
                    className: "headerLinks",
                    children: Object(r.jsxs)("div", {
                        className: "wrap1200".concat(" ", "headerLinksCon"),
                        children: [Object(r.jsx)("div", {
                            children: C ? Object(r.jsxs)("div", {
                                className: "loginBtn".concat(" ", "show"),
                                id: "loginL",
                                children: [Object(r.jsxs)("span", {
                                    id: "welcomeText",
                                    children: ["\u60a8\u597d\uff0c", decodeURIComponent(C), "\u6b22\u8fce\u6765\u5230\u65b0\u4e1c\u65b9"]
                                }), Object(r.jsx)("a", {
                                    href: "http://passport.xdf.cn/Logout.aspx?AppId=32&ReturnUrl=http%3A%2F%2Fwww.xdf.cn%2F",
                                    className: "logoutBtn",
                                    id: "logoutBtn",
                                    target: "_self",
                                    children: "\u9000\u51fa"
                                })]
                            }) : Object(r.jsx)("div", {
                                className: "loginBtn".concat(" show"),
                                id: "loginF",
                                children: Object(r.jsx)("div", {
                                    children: Object(r.jsx)("a", {
                                        href: "https://login.xdf.cn/sso/login?app_id=xdf-edu&redirect_uri=http://www.xdf.cn&response_type=&scope=&state=&ehr_org_id=105",
                                        id: "btn_login",
                                        children: "\u8bf7\u767b\u5f55"
                                    })
                                })
                            })
                        }), Object(r.jsxs)("div", {
                            className: "titleLinks",
                            children: [Object(r.jsx)("div", {
                                className: "titleItem",
                                id: "allschools",
                                children: Object(r.jsx)("a", {
                                    href: "http://xdf.cn",
                                    children: "\u65b0\u4e1c\u65b9\u5b98\u7f51"
                                })
                            }), Object(r.jsxs)("div", {
                                className: "titleItem mbugClass",
                                children: [Object(r.jsx)("a", {
                                    href: "http://i.xdf.cn/",
                                    children: "\u624b\u673a\u8d2d\u8bfe"
                                }), Object(r.jsx)("em", {}), Object(r.jsxs)("div", {
                                    className: "codeCon show",
                                    children: [Object(r.jsx)("img", {
                                        src: "//img.xdf.cn/souke/v8_1/images/minpro.png",
                                        alt: "\u5c0f\u7a0b\u5e8f"
                                    }), Object(r.jsx)("img", {
                                        src: "//img.xdf.cn/souke/v8_1/images/mxdfcn.png",
                                        alt: "h5"
                                    })]
                                })]
                            })]
                        })]
                    })
                }), m ? "" : Object(r.jsx)("div", {
                    className: "bgWhite",
                    children: Object(r.jsxs)("div", {
                        className: "wrap1200".concat(" ", "searchCon"),
                        children: [Object(r.jsxs)("span", {
                            className: "leap-info",
                            onClick: function() {
                                var e, t = {}, n = f(s);
                                try {
                                    for (n.s(); !(e = n.n()).done; ) {
                                        var r = e.value;
                                        parseInt(r.id) === parseInt(Object(d.e)("soukecityid")) && (t = r)
                                    }
                                } catch (o) {
                                    n.e(o)
                                } finally {
                                    n.f()
                                }
                                t.sitePath ? (Object(d.n)("soukecityid", t.id),
                                Object(d.n)("cityName", t.name),
                                window.open("https://www.xdf.cn/".concat(t.sitePath, "/"))) : (Object(d.n)("soukecityid", t.id),
                                Object(d.n)("cityName", t.name),
                                window.open("https://www.xdf.cn/"))
                            },
                            children: [Object(r.jsx)("img", {
                                src: "http://file.xdf.cn/citysite/images/xdfLOGO.png",
                                className: "logo"
                            }), v && Object(r.jsx)("span", {
                                className: "inseachcity",
                                "data-city-select-offset": "[15, 15]",
                                id: "inseachcity",
                                children: v
                            })]
                        }), o && Object(r.jsx)("p", {
                            className: "phone",
                            children: o
                        }), Object(r.jsxs)("div", {
                            className: "searForm",
                            id: "searchBar",
                            children: [Object(r.jsx)("div", {
                                className: "formCon",
                                children: Object(r.jsxs)("div", {
                                    className: "form",
                                    children: [Object(r.jsx)("input", {
                                        type: "text",
                                        value: j,
                                        className: "inpTxt",
                                        id: "txtKeyWord",
                                        placeholder: "\u8bfe\u7a0b\u6216\u73ed\u53f7",
                                        onChange: function(e) {
                                            x(e.target.value)
                                        }
                                    }), Object(r.jsx)("input", {
                                        type: "button",
                                        className: "inpSub",
                                        id: "btnSearchBar",
                                        onClick: function() {
                                            I()
                                        },
                                        value: "\u641c \u7d22"
                                    })]
                                })
                            }), t.length > 0 && Object(r.jsxs)("p", {
                                className: "keyword",
                                id: "keyword",
                                children: ["\u70ed\u95e8\u641c\u7d22\uff1a", t.map((function(e, t) {
                                    return Object(r.jsx)("a", {
                                        href: "/search?cityCode=".concat(n, "&categoryCode=").concat(e.categoryCode),
                                        target: "_blank",
                                        children: e.categoryName
                                    }, "keyword-".concat(t))
                                }
                                ))]
                            })]
                        })]
                    })
                })]
            })
        }
          , y = function() {
            return Object(r.jsx)("div", {
                className: "footer",
                children: Object(r.jsxs)("div", {
                    className: "wrap1200 reserved",
                    children: [Object(r.jsxs)("p", {
                        className: "reservedP",
                        children: ["\u7ecf\u8425\u8bb8\u53ef\u8bc1\u7f16\u53f7\uff1a", Object(r.jsx)("a", {
                            rel: "nofollow",
                            href: "http://beian.miit.gov.cn",
                            target: "_blank",
                            children: "\u4eacICP\u590705067667\u53f7-32"
                        }), " | \u4eacICP\u8bc1060601\u53f7 | \u4eac\u516c\u7f51\u5b89\u590711010802021790\u53f7"]
                    }), Object(r.jsxs)("p", {
                        className: "reservedP",
                        children: ["Copyright 2011-", Object(r.jsx)("span", {
                            id: "nowYear",
                            children: "2021"
                        }), " \u65b0\u4e1c\u65b9\u6559\u80b2\u79d1\u6280\u96c6\u56e2\u6709\u9650\u516c\u53f8, All Rights Reserved"]
                    }), Object(r.jsx)("div", {
                        className: "bottomImgs",
                        id: "kx_logo",
                        children: Object(r.jsx)("a", {
                            href: "https://ss.knet.cn/verifyseal.dll?sn=2011050300100008297&ct=df&a=1&pa=0.12573011522181332",
                            children: Object(r.jsx)("img", {
                                className: "img".concat(" ", "last"),
                                src: "http://file.xdf.cn/201501/cnnic.png",
                                alt: "\u53ef\u4fe1\u7f51\u7ad9"
                            })
                        })
                    })]
                })
            })
        }
          , b = n("20a2");
        function v(e, t) {
            var n;
            if ("undefined" === typeof Symbol || null == e[Symbol.iterator]) {
                if (Array.isArray(e) || (n = function(e, t) {
                    if (!e)
                        return;
                    if ("string" === typeof e)
                        return g(e, t);
                    var n = Object.prototype.toString.call(e).slice(8, -1);
                    "Object" === n && e.constructor && (n = e.constructor.name);
                    if ("Map" === n || "Set" === n)
                        return Array.from(e);
                    if ("Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))
                        return g(e, t)
                }(e)) || t && e && "number" === typeof e.length) {
                    n && (e = n);
                    var r = 0
                      , o = function() {};
                    return {
                        s: o,
                        n: function() {
                            return r >= e.length ? {
                                done: !0
                            } : {
                                done: !1,
                                value: e[r++]
                            }
                        },
                        e: function(e) {
                            throw e
                        },
                        f: o
                    }
                }
                throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
            }
            var a, c = !0, i = !1;
            return {
                s: function() {
                    n = e[Symbol.iterator]()
                },
                n: function() {
                    var e = n.next();
                    return c = e.done,
                    e
                },
                e: function(e) {
                    i = !0,
                    a = e
                },
                f: function() {
                    try {
                        c || null == n.return || n.return()
                    } finally {
                        if (i)
                            throw a
                    }
                }
            }
        }
        function g(e, t) {
            (null == t || t > e.length) && (t = e.length);
            for (var n = 0, r = new Array(t); n < t; n++)
                r[n] = e[n];
            return r
        }
        var w = n("aCH8")
          , j = [];
        t.a = function(e) {
            var t = e.children
              , o = e.siteTitle
              , s = e.siteDescription
              , f = e.cityCode
              , p = e.getSerachClass
              , h = e.kw
              , g = e.parentPhone
              , x = e.deptCode
              , O = e.getCityName
              , C = e.getConnectionConfig
              , k = e.page
              , S = e.categoryCode
              , _ = Object(i.useState)([])
              , A = _[0]
              , I = _[1]
              , N = Object(i.useState)([])
              , M = N[0]
              , T = N[1]
              , P = Object(i.useState)([])
              , B = P[0]
              , E = P[1]
              , H = Object(i.useState)({})
              , F = (H[0],
            H[1],
            Object(b.useRouter)())
              , q = !!e.isHiddenHeaderSearch && e.isHiddenHeaderSearch;
            Object(i.useEffect)((function() {
                var e = /Android|webOS|iPhone|Windows Phone|iPod|BlackBerry|SymbianOS/i.test(navigator.userAgent);
                if (e && (0 == window.location.pathname.indexOf("/area/") || 0 == window.location.pathname.indexOf("/item/") || 0 == window.location.pathname.indexOf("/search"))) {
                    var t = "".concat(l.e).concat(window.location.pathname).concat(window.location.pathname.indexOf(".html") > 0 ? "" : ".html").concat(window.location.search);
                    window.location.href = t
                }
                if (e && 0 == window.location.pathname.indexOf("/search")) {
                    var n = "".concat(l.e).concat(window.location.pathname).concat(window.location.search);
                    window.location.href = n
                }
                L()
            }
            ), []),
            Object(i.useEffect)((function() {
                g && I(g)
            }
            ), [g]);
            var L = function() {
                var e = Object(c.a)(a.a.mark((function e() {
                    var t, n, r, o, c, i, s, u, l, f, p, h, m, y, b;
                    return a.a.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (!(t = window.location.href.match(/\/(item|area)\/(.*?)\.html/)) || !t[2]) {
                                    e.next = 35;
                                    break
                                }
                                if (n = t[2].split("-"),
                                !("item" == t[1] && n[1] && n[2] && n[0] && n[0].length < 6)) {
                                    e.next = 11;
                                    break
                                }
                                return e.next = 6,
                                window.xdfCommonCitySelect.getCityListAsync();
                            case 6:
                                o = e.sent,
                                c = null === (r = o.find((function(e) {
                                    return e.id == n[0] || e.code == n[0]
                                }
                                ))) || void 0 === r ? void 0 : r.code,
                                window.location.replace("".concat(window.location.origin, "/item/").concat(c || "", "-").concat(n[1], "-").concat(n[2], ".html")),
                                e.next = 35;
                                break;
                            case 11:
                                if ("area" != t[1]) {
                                    e.next = 35;
                                    break
                                }
                                return e.next = 14,
                                window.xdfCommonCitySelect.getCityListAsync();
                            case 14:
                                if (i = e.sent,
                                n[1] && n[2] && n[0].length < 6 && (u = null === (s = i.find((function(e) {
                                    return e.id == n[0] || e.code == n[0]
                                }
                                ))) || void 0 === s ? void 0 : s.code,
                                window.location.replace("".concat(window.location.origin, "/area/").concat(u, "-").concat(n[1], "-").concat(n[2], ".html"))),
                                n[1] || n[2] || !(n[0].length < 6)) {
                                    e.next = 35;
                                    break
                                }
                                if ("0" != n[0]) {
                                    e.next = 30;
                                    break
                                }
                                if (!(l = Object(d.e)("cityCode"))) {
                                    e.next = 27;
                                    break
                                }
                                return e.next = 22,
                                window.xdfCommonCitySelect.getCityListAsync();
                            case 22:
                                p = e.sent,
                                h = null === (f = p.find((function(e) {
                                    return e.id == l || e.code == l
                                }
                                ))) || void 0 === f ? void 0 : f.code,
                                window.location.replace("".concat(window.location.origin, "/area/").concat(h, ".html")),
                                e.next = 28;
                                break;
                            case 27:
                                window.location.replace("https://www.xdf.cn?redirectUrl=".concat(encodeURIComponent(window.location.href.replace("/0.html", "/{cityId}.html"))));
                            case 28:
                                e.next = 35;
                                break;
                            case 30:
                                return e.next = 32,
                                window.xdfCommonCitySelect.getCityListAsync();
                            case 32:
                                y = e.sent,
                                b = null === (m = y.find((function(e) {
                                    return e.id == n[0] || e.code == n[0]
                                }
                                ))) || void 0 === m ? void 0 : m.code,
                                window.location.replace("".concat(window.location.origin, "/area/").concat(b, ".html"));
                            case 35:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )));
                return function() {
                    return e.apply(this, arguments)
                }
            }()
              , R = function() {
                var e = Object(c.a)(a.a.mark((function e() {
                    var t, n, r, o;
                    return a.a.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (f) {
                                    e.next = 2;
                                    break
                                }
                                return e.abrupt("return", !1);
                            case 2:
                                return t = "appId=".concat(l.a, "&cityCode=").concat(f, "&t=").concat((new Date).getTime()),
                                n = w("".concat(t).concat(l.b)),
                                e.next = 6,
                                fetch("".concat(l.d, "/portal/v1/pc/city/list?").concat(t), {
                                    headers: {
                                        "Content-Type": "application/json",
                                        sign: n
                                    }
                                });
                            case 6:
                                return r = e.sent,
                                e.next = 9,
                                r.json();
                            case 9:
                                (o = e.sent).status && 1 == o.status && o.data && E(o.data || []);
                            case 11:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )));
                return function() {
                    return e.apply(this, arguments)
                }
            }()
              , U = function() {
                var e = Object(c.a)(a.a.mark((function e() {
                    return a.a.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (f) {
                                    e.next = 2;
                                    break
                                }
                                return e.abrupt("return");
                            case 2:
                                Object(c.a)(a.a.mark((function e() {
                                    return a.a.wrap((function(e) {
                                        for (; ; )
                                            switch (e.prev = e.next) {
                                            case 0:
                                                return e.next = 2,
                                                n.e(33).then(n.bind(null, "BMYk"));
                                            case 2:
                                                return e.abrupt("return", e.sent.default);
                                            case 3:
                                            case "end":
                                                return e.stop()
                                            }
                                    }
                                    ), e)
                                }
                                )))().then((function(e) {
                                    e().get("".concat(l.d, "/portal/v2/hot-keyword/list"), {
                                        params: {
                                            cityCode: f,
                                            categoryCode: S
                                        }
                                    }).then((function(e) {
                                        "200" == e.data.code && T(e.data.data || [])
                                    }
                                    )).catch((function(e) {
                                        console.log(e)
                                    }
                                    ))
                                }
                                ));
                            case 3:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )));
                return function() {
                    return e.apply(this, arguments)
                }
            }()
              , D = function() {
                var e = Object(c.a)(a.a.mark((function e() {
                    var t, n, r, o, c, i, s, u, f;
                    return a.a.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (window.gio) {
                                    e.next = 3;
                                    break
                                }
                                return setTimeout((function() {
                                    D()
                                }
                                ), 500),
                                e.abrupt("return");
                            case 3:
                                t = F.pathname,
                                n = "",
                                e.t0 = t,
                                e.next = "/area/[id]" === e.t0 ? 8 : "/search" === e.t0 ? 10 : "/item/[id]" === e.t0 ? 13 : 15;
                                break;
                            case 8:
                                return n = "\u9996\u9875",
                                e.abrupt("break", 16);
                            case 10:
                                return n = "\u73ed\u7ea7\u5217\u8868",
                                Object.keys(F.query).hasOwnProperty("kw") && (n = "\u641c\u7d22\u7ed3\u679c"),
                                e.abrupt("break", 16);
                            case 13:
                                return n = "\u73ed\u7ea7\u8be6\u60c5",
                                e.abrupt("break", 16);
                            case 15:
                                return e.abrupt("break", 16);
                            case 16:
                                "PC",
                                r = "";
                                try {
                                    if (n)
                                        try {
                                            gio("page.set", {
                                                pagetype: n
                                            })
                                        } catch (a) {
                                            console.log("err", a)
                                        }
                                    if (F.query) {
                                        o = "",
                                        F.query.schoolId ? o = F.query.schoolId : F.query.id ? (c = String(F.query.id).split("-"),
                                        o = c[1]) : o = F.query.cityCode;
                                        try {
                                            gio("visitor.set", {
                                                schoolid: o,
                                                platform: "PC"
                                            })
                                        } catch (a) {
                                            console.log("err", a)
                                        }
                                    }
                                } catch (a) {
                                    console.log(a)
                                }
                                return i = Object(d.e)("U2AT"),
                                s = w("/common/check/wx?14e1b600b1fd579f47433b88e8d85291"),
                                e.prev = 21,
                                e.next = 24,
                                fetch("".concat(l.c, "/common/check/wx"), {
                                    headers: {
                                        "Content-Type": "application/json",
                                        sign: s,
                                        appId: "api_app_wechat"
                                    }
                                });
                            case 24:
                                return u = e.sent,
                                e.next = 27,
                                u.json();
                            case 27:
                                200 == (f = e.sent).code && f.data && (r = f.data.userId,
                                window.xdfCommonReportData.sendLoginInfo({
                                    U2AT: i,
                                    U2userId: r
                                })),
                                e.next = 34;
                                break;
                            case 31:
                                e.prev = 31,
                                e.t1 = e.catch(21),
                                console.log(e.t1);
                            case 34:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e, null, [[21, 31]])
                }
                )));
                return function() {
                    return e.apply(this, arguments)
                }
            }();
            Object(i.useEffect)((function() {
                D(),
                R()
            }
            ), []),
            Object(i.useEffect)((function() {
                U()
            }
            ), [S]),
            Object(i.useEffect)((function() {
                B.forEach((function(e) {
                    e.code == f && O && O(e.name)
                }
                ))
            }
            ), [B]),
            Object(i.useEffect)((function() {
                (function(e) {
                    if (j.length != e.length)
                        return j = e,
                        !1;
                    var t, n = v(e);
                    try {
                        var r = function() {
                            var n = t.value;
                            if (j.findIndex((function(e) {
                                return e == n
                            }
                            )) < 0)
                                return j = e,
                                {
                                    v: !1
                                }
                        };
                        for (n.s(); !(t = n.n()).done; ) {
                            var o = r();
                            if ("object" === typeof o)
                                return o.v
                        }
                    } catch (a) {
                        n.e(a)
                    } finally {
                        n.f()
                    }
                    return !0
                }
                )(x || []) || W()
            }
            ), [x]);
            var W = function() {
                if (f && x) {
                    var e = F.pathname;
                    if (!("/item/[id]" != e && "/search" != e || q)) {
                        var t = "class_list";
                        switch (e) {
                        case "/search":
                            t = "class_list";
                            break;
                        case "/item/[id]":
                            t = "class_detail";
                            break;
                        default:
                            t = "class_list"
                        }
                        var n = {
                            mode: "pc",
                            pageType: t,
                            client: "xdf_pc",
                            deptCode: x,
                            showItems: {
                                pc: ["hotline", "onlineService", "form", "wechatQr"]
                            },
                            cityCode: f
                        };
                        window.xdfCommonConnection.init(n).then((function(e) {
                            var n, r;
                            (C && C(e || {}),
                            e) && ("class_detail" === t && null !== (n = e.hotlineList[0]) && void 0 !== n && n.telephone && I(null === (r = e.hotlineList[0]) || void 0 === r ? void 0 : r.telephone))
                        }
                        ))
                    }
                }
            };
            return Object(r.jsxs)("div", {
                className: "container",
                children: [Object(r.jsxs)(u.a, {
                    children: [Object(r.jsx)("link", {
                        rel: "icon",
                        href: "/favicon.ico"
                    }), Object(r.jsx)("meta", {
                        name: "description",
                        content: s || "\u65b0\u4e1c\u65b9\u7f51\uff08www.xdf.cn\uff09\u662f\u65b0\u4e1c\u65b9\u6559\u80b2\u79d1\u6280\u96c6\u56e2\u63a8\u51fa\u7684\u4e00\u7ad9\u5f0f\u5b66\u4e60\u4e92\u52a8\u4ea4\u6d41\u5e73\u53f0\uff0c\u65b0\u4e1c\u65b9\u7f51\u7684\u5185\u5bb9\u6db5\u76d6\u4e86\u82f1\u8bed\u5b66\u4e60\u89c4\u5212\u3001\u6210\u957f\u5bfc\u822a\u3001\u65b0\u4e1c\u65b9\u641c\u8bfe\u3001\u65b0\u4e1c\u65b9\u8001\u5e08\u7b54\u95ee\u3001\u5728\u7ebf\u54a8\u8be2\u3001\u7f51\u4e0a\u6d4b\u8bc4\u3001\u5b66\u4e60\u8d44\u8baf\u3001\u65b0\u4e1c\u65b9\u5b66\u5458\u670d\u52a1\u3001\u65b0\u4e1c\u65b9\u793e\u533a\u7b49\uff0c\u66f4\u591a\u7cbe\u5f69\u5185\u5bb9\u5c3d\u5728\u65b0\u4e1c\u65b9\u7f51\u3002"
                    }), Object(r.jsx)("meta", {
                        property: "og:image",
                        content: "https://og-image.now.sh/".concat(encodeURI(o), ".png?theme=light&md=0&fontSize=75px&images=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Ffront%2Fassets%2Fdesign%2Fnextjs-black-logo.svg")
                    }), Object(r.jsx)("meta", {
                        name: "og:title",
                        content: o
                    }), Object(r.jsx)("meta", {
                        content: "always",
                        name: "referrer"
                    }), Object(r.jsx)("meta", {
                        name: "twitter:card",
                        content: "summary_large_image"
                    }), Object(r.jsx)("title", {
                        children: o
                    })]
                }), Object(r.jsxs)("div", {
                    children: [!q && Object(r.jsx)(m, {
                        hotKeywordList: M,
                        cityCode: f,
                        telephone: A,
                        cityList: B,
                        getSerachClass: p,
                        kw: h,
                        isHiddenHeaderSearch: q,
                        page: k
                    }), Object(r.jsx)("main", {
                        children: t
                    }), Object(r.jsx)(y, {})]
                })]
            })
        }
    },
    "5fIB": function(e, t, n) {
        var r = n("7eYB");
        e.exports = function(e) {
            if (Array.isArray(e))
                return r(e)
        }
    },
    "8Kt/": function(e, t, n) {
        "use strict";
        var r = n("oI91");
        function o(e, t) {
            var n = Object.keys(e);
            if (Object.getOwnPropertySymbols) {
                var r = Object.getOwnPropertySymbols(e);
                t && (r = r.filter((function(t) {
                    return Object.getOwnPropertyDescriptor(e, t).enumerable
                }
                ))),
                n.push.apply(n, r)
            }
            return n
        }
        t.__esModule = !0,
        t.defaultHead = f,
        t.default = void 0;
        var a, c = function(e) {
            if (e && e.__esModule)
                return e;
            if (null === e || "object" !== typeof e && "function" !== typeof e)
                return {
                    default: e
                };
            var t = l();
            if (t && t.has(e))
                return t.get(e);
            var n = {}
              , r = Object.defineProperty && Object.getOwnPropertyDescriptor;
            for (var o in e)
                if (Object.prototype.hasOwnProperty.call(e, o)) {
                    var a = r ? Object.getOwnPropertyDescriptor(e, o) : null;
                    a && (a.get || a.set) ? Object.defineProperty(n, o, a) : n[o] = e[o]
                }
            n.default = e,
            t && t.set(e, n);
            return n
        }(n("q1tI")), i = (a = n("Xuae")) && a.__esModule ? a : {
            default: a
        }, s = n("lwAK"), u = n("FYa8"), d = n("/0+H");
        function l() {
            if ("function" !== typeof WeakMap)
                return null;
            var e = new WeakMap;
            return l = function() {
                return e
            }
            ,
            e
        }
        function f() {
            var e = arguments.length > 0 && void 0 !== arguments[0] && arguments[0]
              , t = [c.default.createElement("meta", {
                charSet: "utf-8"
            })];
            return e || t.push(c.default.createElement("meta", {
                name: "viewport",
                content: "width=device-width"
            })),
            t
        }
        function p(e, t) {
            return "string" === typeof t || "number" === typeof t ? e : t.type === c.default.Fragment ? e.concat(c.default.Children.toArray(t.props.children).reduce((function(e, t) {
                return "string" === typeof t || "number" === typeof t ? e : e.concat(t)
            }
            ), [])) : e.concat(t)
        }
        var h = ["name", "httpEquiv", "charSet", "itemProp"];
        function m(e, t) {
            return e.reduce((function(e, t) {
                var n = c.default.Children.toArray(t.props.children);
                return e.concat(n)
            }
            ), []).reduce(p, []).reverse().concat(f(t.inAmpMode)).filter(function() {
                var e = new Set
                  , t = new Set
                  , n = new Set
                  , r = {};
                return function(o) {
                    var a = !0
                      , c = !1;
                    if (o.key && "number" !== typeof o.key && o.key.indexOf("$") > 0) {
                        c = !0;
                        var i = o.key.slice(o.key.indexOf("$") + 1);
                        e.has(i) ? a = !1 : e.add(i)
                    }
                    switch (o.type) {
                    case "title":
                    case "base":
                        t.has(o.type) ? a = !1 : t.add(o.type);
                        break;
                    case "meta":
                        for (var s = 0, u = h.length; s < u; s++) {
                            var d = h[s];
                            if (o.props.hasOwnProperty(d))
                                if ("charSet" === d)
                                    n.has(d) ? a = !1 : n.add(d);
                                else {
                                    var l = o.props[d]
                                      , f = r[d] || new Set;
                                    "name" === d && c || !f.has(l) ? (f.add(l),
                                    r[d] = f) : a = !1
                                }
                        }
                    }
                    return a
                }
            }()).reverse().map((function(e, n) {
                var a = e.key || n;
                if (!t.inAmpMode && "link" === e.type && e.props.href && ["https://fonts.googleapis.com/css"].some((function(t) {
                    return e.props.href.startsWith(t)
                }
                ))) {
                    var i = function(e) {
                        for (var t = 1; t < arguments.length; t++) {
                            var n = null != arguments[t] ? arguments[t] : {};
                            t % 2 ? o(Object(n), !0).forEach((function(t) {
                                r(e, t, n[t])
                            }
                            )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(n)) : o(Object(n)).forEach((function(t) {
                                Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(n, t))
                            }
                            ))
                        }
                        return e
                    }({}, e.props || {});
                    return i["data-href"] = i.href,
                    i.href = void 0,
                    c.default.cloneElement(e, i)
                }
                return c.default.cloneElement(e, {
                    key: a
                })
            }
            ))
        }
        function y(e) {
            var t = e.children
              , n = (0,
            c.useContext)(s.AmpStateContext)
              , r = (0,
            c.useContext)(u.HeadManagerContext);
            return c.default.createElement(i.default, {
                reduceComponentsToState: m,
                headManager: r,
                inAmpMode: (0,
                d.isInAmpMode)(n)
            }, t)
        }
        y.rewind = function() {}
        ;
        var b = y;
        t.default = b
    },
    ANhw: function(e, t) {
        !function() {
            var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
              , n = {
                rotl: function(e, t) {
                    return e << t | e >>> 32 - t
                },
                rotr: function(e, t) {
                    return e << 32 - t | e >>> t
                },
                endian: function(e) {
                    if (e.constructor == Number)
                        return 16711935 & n.rotl(e, 8) | 4278255360 & n.rotl(e, 24);
                    for (var t = 0; t < e.length; t++)
                        e[t] = n.endian(e[t]);
                    return e
                },
                randomBytes: function(e) {
                    for (var t = []; e > 0; e--)
                        t.push(Math.floor(256 * Math.random()));
                    return t
                },
                bytesToWords: function(e) {
                    for (var t = [], n = 0, r = 0; n < e.length; n++,
                    r += 8)
                        t[r >>> 5] |= e[n] << 24 - r % 32;
                    return t
                },
                wordsToBytes: function(e) {
                    for (var t = [], n = 0; n < 32 * e.length; n += 8)
                        t.push(e[n >>> 5] >>> 24 - n % 32 & 255);
                    return t
                },
                bytesToHex: function(e) {
                    for (var t = [], n = 0; n < e.length; n++)
                        t.push((e[n] >>> 4).toString(16)),
                        t.push((15 & e[n]).toString(16));
                    return t.join("")
                },
                hexToBytes: function(e) {
                    for (var t = [], n = 0; n < e.length; n += 2)
                        t.push(parseInt(e.substr(n, 2), 16));
                    return t
                },
                bytesToBase64: function(e) {
                    for (var n = [], r = 0; r < e.length; r += 3)
                        for (var o = e[r] << 16 | e[r + 1] << 8 | e[r + 2], a = 0; a < 4; a++)
                            8 * r + 6 * a <= 8 * e.length ? n.push(t.charAt(o >>> 6 * (3 - a) & 63)) : n.push("=");
                    return n.join("")
                },
                base64ToBytes: function(e) {
                    e = e.replace(/[^A-Z0-9+\/]/gi, "");
                    for (var n = [], r = 0, o = 0; r < e.length; o = ++r % 4)
                        0 != o && n.push((t.indexOf(e.charAt(r - 1)) & Math.pow(2, -2 * o + 8) - 1) << 2 * o | t.indexOf(e.charAt(r)) >>> 6 - 2 * o);
                    return n
                }
            };
            e.exports = n
        }()
    },
    BEtg: function(e, t) {
        function n(e) {
            return !!e.constructor && "function" === typeof e.constructor.isBuffer && e.constructor.isBuffer(e)
        }
        e.exports = function(e) {
            return null != e && (n(e) || function(e) {
                return "function" === typeof e.readFloatLE && "function" === typeof e.slice && n(e.slice(0, 0))
            }(e) || !!e._isBuffer)
        }
    },
    FYa8: function(e, t, n) {
        "use strict";
        var r;
        t.__esModule = !0,
        t.HeadManagerContext = void 0;
        var o = ((r = n("q1tI")) && r.__esModule ? r : {
            default: r
        }).default.createContext({});
        t.HeadManagerContext = o
    },
    T0f4: function(e, t) {
        function n(t) {
            return e.exports = n = Object.setPrototypeOf ? Object.getPrototypeOf : function(e) {
                return e.__proto__ || Object.getPrototypeOf(e)
            }
            ,
            n(t)
        }
        e.exports = n
    },
    Xuae: function(e, t, n) {
        "use strict";
        var r = n("mPvQ")
          , o = n("/GRZ")
          , a = n("i2R6")
          , c = (n("qXWd"),
        n("48fX"))
          , i = n("tCBg")
          , s = n("T0f4");
        function u(e) {
            var t = function() {
                if ("undefined" === typeof Reflect || !Reflect.construct)
                    return !1;
                if (Reflect.construct.sham)
                    return !1;
                if ("function" === typeof Proxy)
                    return !0;
                try {
                    return Date.prototype.toString.call(Reflect.construct(Date, [], (function() {}
                    ))),
                    !0
                } catch (e) {
                    return !1
                }
            }();
            return function() {
                var n, r = s(e);
                if (t) {
                    var o = s(this).constructor;
                    n = Reflect.construct(r, arguments, o)
                } else
                    n = r.apply(this, arguments);
                return i(this, n)
            }
        }
        t.__esModule = !0,
        t.default = void 0;
        var d = n("q1tI")
          , l = function(e) {
            c(n, e);
            var t = u(n);
            function n(e) {
                var a;
                return o(this, n),
                (a = t.call(this, e))._hasHeadManager = void 0,
                a.emitChange = function() {
                    a._hasHeadManager && a.props.headManager.updateHead(a.props.reduceComponentsToState(r(a.props.headManager.mountedInstances), a.props))
                }
                ,
                a._hasHeadManager = a.props.headManager && a.props.headManager.mountedInstances,
                a
            }
            return a(n, [{
                key: "componentDidMount",
                value: function() {
                    this._hasHeadManager && this.props.headManager.mountedInstances.add(this),
                    this.emitChange()
                }
            }, {
                key: "componentDidUpdate",
                value: function() {
                    this.emitChange()
                }
            }, {
                key: "componentWillUnmount",
                value: function() {
                    this._hasHeadManager && this.props.headManager.mountedInstances.delete(this),
                    this.emitChange()
                }
            }, {
                key: "render",
                value: function() {
                    return null
                }
            }]),
            n
        }(d.Component);
        t.default = l
    },
    aCH8: function(e, t, n) {
        !function() {
            var t = n("ANhw")
              , r = n("mmNF").utf8
              , o = n("BEtg")
              , a = n("mmNF").bin
              , c = function(e, n) {
                e.constructor == String ? e = n && "binary" === n.encoding ? a.stringToBytes(e) : r.stringToBytes(e) : o(e) ? e = Array.prototype.slice.call(e, 0) : Array.isArray(e) || e.constructor === Uint8Array || (e = e.toString());
                for (var i = t.bytesToWords(e), s = 8 * e.length, u = 1732584193, d = -271733879, l = -1732584194, f = 271733878, p = 0; p < i.length; p++)
                    i[p] = 16711935 & (i[p] << 8 | i[p] >>> 24) | 4278255360 & (i[p] << 24 | i[p] >>> 8);
                i[s >>> 5] |= 128 << s % 32,
                i[14 + (s + 64 >>> 9 << 4)] = s;
                var h = c._ff
                  , m = c._gg
                  , y = c._hh
                  , b = c._ii;
                for (p = 0; p < i.length; p += 16) {
                    var v = u
                      , g = d
                      , w = l
                      , j = f;
                    u = h(u, d, l, f, i[p + 0], 7, -680876936),
                    f = h(f, u, d, l, i[p + 1], 12, -389564586),
                    l = h(l, f, u, d, i[p + 2], 17, 606105819),
                    d = h(d, l, f, u, i[p + 3], 22, -1044525330),
                    u = h(u, d, l, f, i[p + 4], 7, -176418897),
                    f = h(f, u, d, l, i[p + 5], 12, 1200080426),
                    l = h(l, f, u, d, i[p + 6], 17, -1473231341),
                    d = h(d, l, f, u, i[p + 7], 22, -45705983),
                    u = h(u, d, l, f, i[p + 8], 7, 1770035416),
                    f = h(f, u, d, l, i[p + 9], 12, -1958414417),
                    l = h(l, f, u, d, i[p + 10], 17, -42063),
                    d = h(d, l, f, u, i[p + 11], 22, -1990404162),
                    u = h(u, d, l, f, i[p + 12], 7, 1804603682),
                    f = h(f, u, d, l, i[p + 13], 12, -40341101),
                    l = h(l, f, u, d, i[p + 14], 17, -1502002290),
                    u = m(u, d = h(d, l, f, u, i[p + 15], 22, 1236535329), l, f, i[p + 1], 5, -165796510),
                    f = m(f, u, d, l, i[p + 6], 9, -1069501632),
                    l = m(l, f, u, d, i[p + 11], 14, 643717713),
                    d = m(d, l, f, u, i[p + 0], 20, -373897302),
                    u = m(u, d, l, f, i[p + 5], 5, -701558691),
                    f = m(f, u, d, l, i[p + 10], 9, 38016083),
                    l = m(l, f, u, d, i[p + 15], 14, -660478335),
                    d = m(d, l, f, u, i[p + 4], 20, -405537848),
                    u = m(u, d, l, f, i[p + 9], 5, 568446438),
                    f = m(f, u, d, l, i[p + 14], 9, -1019803690),
                    l = m(l, f, u, d, i[p + 3], 14, -187363961),
                    d = m(d, l, f, u, i[p + 8], 20, 1163531501),
                    u = m(u, d, l, f, i[p + 13], 5, -1444681467),
                    f = m(f, u, d, l, i[p + 2], 9, -51403784),
                    l = m(l, f, u, d, i[p + 7], 14, 1735328473),
                    u = y(u, d = m(d, l, f, u, i[p + 12], 20, -1926607734), l, f, i[p + 5], 4, -378558),
                    f = y(f, u, d, l, i[p + 8], 11, -2022574463),
                    l = y(l, f, u, d, i[p + 11], 16, 1839030562),
                    d = y(d, l, f, u, i[p + 14], 23, -35309556),
                    u = y(u, d, l, f, i[p + 1], 4, -1530992060),
                    f = y(f, u, d, l, i[p + 4], 11, 1272893353),
                    l = y(l, f, u, d, i[p + 7], 16, -155497632),
                    d = y(d, l, f, u, i[p + 10], 23, -1094730640),
                    u = y(u, d, l, f, i[p + 13], 4, 681279174),
                    f = y(f, u, d, l, i[p + 0], 11, -358537222),
                    l = y(l, f, u, d, i[p + 3], 16, -722521979),
                    d = y(d, l, f, u, i[p + 6], 23, 76029189),
                    u = y(u, d, l, f, i[p + 9], 4, -640364487),
                    f = y(f, u, d, l, i[p + 12], 11, -421815835),
                    l = y(l, f, u, d, i[p + 15], 16, 530742520),
                    u = b(u, d = y(d, l, f, u, i[p + 2], 23, -995338651), l, f, i[p + 0], 6, -198630844),
                    f = b(f, u, d, l, i[p + 7], 10, 1126891415),
                    l = b(l, f, u, d, i[p + 14], 15, -1416354905),
                    d = b(d, l, f, u, i[p + 5], 21, -57434055),
                    u = b(u, d, l, f, i[p + 12], 6, 1700485571),
                    f = b(f, u, d, l, i[p + 3], 10, -1894986606),
                    l = b(l, f, u, d, i[p + 10], 15, -1051523),
                    d = b(d, l, f, u, i[p + 1], 21, -2054922799),
                    u = b(u, d, l, f, i[p + 8], 6, 1873313359),
                    f = b(f, u, d, l, i[p + 15], 10, -30611744),
                    l = b(l, f, u, d, i[p + 6], 15, -1560198380),
                    d = b(d, l, f, u, i[p + 13], 21, 1309151649),
                    u = b(u, d, l, f, i[p + 4], 6, -145523070),
                    f = b(f, u, d, l, i[p + 11], 10, -1120210379),
                    l = b(l, f, u, d, i[p + 2], 15, 718787259),
                    d = b(d, l, f, u, i[p + 9], 21, -343485551),
                    u = u + v >>> 0,
                    d = d + g >>> 0,
                    l = l + w >>> 0,
                    f = f + j >>> 0
                }
                return t.endian([u, d, l, f])
            };
            c._ff = function(e, t, n, r, o, a, c) {
                var i = e + (t & n | ~t & r) + (o >>> 0) + c;
                return (i << a | i >>> 32 - a) + t
            }
            ,
            c._gg = function(e, t, n, r, o, a, c) {
                var i = e + (t & r | n & ~r) + (o >>> 0) + c;
                return (i << a | i >>> 32 - a) + t
            }
            ,
            c._hh = function(e, t, n, r, o, a, c) {
                var i = e + (t ^ n ^ r) + (o >>> 0) + c;
                return (i << a | i >>> 32 - a) + t
            }
            ,
            c._ii = function(e, t, n, r, o, a, c) {
                var i = e + (n ^ (t | ~r)) + (o >>> 0) + c;
                return (i << a | i >>> 32 - a) + t
            }
            ,
            c._blocksize = 16,
            c._digestsize = 16,
            e.exports = function (e, n) {
                if (void 0 === e || null === e)
                    throw new Error("Illegal argument " + e);
                var r = t.wordsToBytes(c(e, n));
                return n && n.asBytes ? r : n && n.asString ? a.bytesToString(r) : t.bytesToHex(r)
            }
        }()
    },
    g4pe: function(e, t, n) {
        e.exports = n("8Kt/")
    },
    iFgM: function(e, t, n) {},
    kG2m: function(e, t) {
        e.exports = function() {
            throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
        }
    },
    lwAK: function(e, t, n) {
        "use strict";
        var r;
        t.__esModule = !0,
        t.AmpStateContext = void 0;
        var o = ((r = n("q1tI")) && r.__esModule ? r : {
            default: r
        }).default.createContext({});
        t.AmpStateContext = o
    },
    mPvQ: function(e, t, n) {
        var r = n("5fIB")
          , o = n("rlHP")
          , a = n("KckH")
          , c = n("kG2m");
        e.exports = function(e) {
            return r(e) || o(e) || a(e) || c()
        }
    },
    mmNF: function(e, t) {
        var n = {
            utf8: {
                stringToBytes: function(e) {
                    return n.bin.stringToBytes(unescape(encodeURIComponent(e)))
                },
                bytesToString: function(e) {
                    return decodeURIComponent(escape(n.bin.bytesToString(e)))
                }
            },
            bin: {
                stringToBytes: function(e) {
                    for (var t = [], n = 0; n < e.length; n++)
                        t.push(255 & e.charCodeAt(n));
                    return t
                },
                bytesToString: function(e) {
                    for (var t = [], n = 0; n < e.length; n++)
                        t.push(String.fromCharCode(e[n]));
                    return t.join("")
                }
            }
        };
        e.exports = n
    },
    qXWd: function(e, t) {
        e.exports = function(e) {
            if (void 0 === e)
                throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
            return e
        }
    },
    tCBg: function(e, t, n) {
        var r = n("C+bE")
          , o = n("qXWd");
        e.exports = function(e, t) {
            return !t || "object" !== r(t) && "function" !== typeof t ? o(e) : t
        }
    }
}]);
