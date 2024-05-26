window = global

delete global
delete Buffer

window.requestAnimationFrame = function () {
}
document = {}
navigator = {}

XMLHttpRequest = function () {
}

function SetProxy(proxyObjs) {
    for (let i = 0; i < proxyObjs.length; i++) {
        const handler = `{
          get: function(target, property, receiver) {
            console.log("方法:", "get  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", target[property]);
            return target[property];
          },
          set: function(target, property, value, receiver) {
            console.log("方法:", "set  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", value, ", 属性值类型：", typeof target[property]);
            return Reflect.set(...arguments);
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

SetProxy(["window", "document", "location", "navigator", "localStorage", "screen"])
