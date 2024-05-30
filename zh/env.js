window = global;

delete global;
delete Buffer;

window.__ZH__ = {
  zse: {
    zk: [
       1170614578,  1024848638,  1413669199,
       -343334464,  -766094290, -1373058082,
       -143119608,  -297228157,  1933479194,
       -971186181,  -406453910,   460404854,
       -547427574, -1891326262, -1679095901,
       2119585428, -2029270069,  2035090028,
      -1521520070,    -5587175,   -77751101,
      -2094365853, -1243052806,  1579901135,
       1321810770,   456816404, -1391643889,
       -229302305,   330002838,  -788960546,
        363569021, -1947871109
    ]
  }
}
window.name = ''
window.alert = function() {}


netor0x86 = {}

Math.random = function() {
    return 0.1
}

navigator = {
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    toString: function() {
        return '[object Navigator]'
    },
    webdriver: false
}
CanvasRenderingContext2D = {
    toString: function() {
        return 'function CanvasRenderingContext2D() { [native code] }'
    }
}
canvas = {
    getContext: function() {
        return CanvasRenderingContext2D
    }
}
document = {
    toString: function() {
        return '[object HTMLDocument]'
    },
    createElement:function(element) {
        console.log('element::::', element)
        return canvas
    },
    getElementById: function() { return {} },
    getElementsByClassName: function() { return {} }
}
location = {
    toString: function() {
        return 'https://zhuanlan.zhihu.com/p/641597841'
    },
    href: 'https://zhuanlan.zhihu.com/p/641597841'
}
screen = {
    toString: function() {
        return '[object Screen]'
    }
}
history = {
    toString: function() {
        return '[object History]'
    }
}

function SetProxy(proxyObjs) {
    for (let i = 0; i < proxyObjs.length; i++) {
        const handler = `{
          get: function(target, property, receiver) {
            if (property !== 'webpackChunkheifetz' && property != '__ZH__') {
              console.log("方法:", "get  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", target[property]);
            }
            return target[property];
          }
        }`;
        eval(`try {
            ${proxyObjs[i]};
            ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
        } catch (e) {
            ${proxyObjs[i]} = {};
            ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
        }`);
    }
}

SetProxy(["window", "document", "location", "navigator","localStorage", "screen", 'history', 'canvas', 'CanvasRenderingContext2D'])
