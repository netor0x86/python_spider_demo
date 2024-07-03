require('./env')
require('./loader')
require('./module')


t = '6key_web_new_fanyi6dVjYLFyzfkFkkapple'

a = window.loader(68214)
u = window.loader.n(a)
// console.log(u()(t).toString().substring(0, 16))
function get_sign(t) {
    return u()("6key_web_new_fanyi6dVjYLFyzfkFkk".concat(t.replace(/(^\s*)|(\s*$)/g, ""))).toString().substring(0, 16)
}

console.log(get_sign('apple'))