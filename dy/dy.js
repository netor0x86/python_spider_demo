require('./env')
require('./source')


function get_a_b(p) {
    arguments = [
        0,
        1,
        14,
        p,
        "",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ]
    var r = window.func._v;
    return (0, window.func._u)(r[0], arguments, r[1], r[2], this)
}

// p = "device_platform=webapp&aid=6383&channel=channel_pc_web&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=124.0.0.0&browser_online=true&engine_name=Blink&engine_version=124.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=4&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7368633937193813504&msToken=LzB7u-2OQf2nT4plB2GeR8R6jh0XU0lwFsIiHKByyzPRfiG83bNex8j9Xvh24f_-czpOPnyjD9GGfWW2etgr71YArbdPZpdisNA9OP4Jgq8xH-Ty9p-kL8293Rfe0g%3D%3D&msToken=LzB7u-2OQf2nT4plB2GeR8R6jh0XU0lwFsIiHKByyzPRfiG83bNex8j9Xvh24f_-czpOPnyjD9GGfWW2etgr71YArbdPZpdisNA9OP4Jgq8xH-Ty9p-kL8293Rfe0g%3D%3D"
// ab = get_a_b(p)
// console.log(ab, '->', ab.length)