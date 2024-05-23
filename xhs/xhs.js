require("./env")
require("./source")

function get_headers(c, i) {
    return window._webmsxyw(c, i)
}
c = '/api/sns/web/v1/homefeed'
i = {
    "cursor_score": "",
    "num": 19,
    "refresh_type": 1,
    "note_index": 35,
    "unread_begin_note_id": "",
    "unread_end_note_id": "",
    "unread_note_count": 0,
    "category": "homefeed.food_v3",
    "search_key": "",
    "need_num": 4,
    "image_formats": [
        "jpg",
        "webp",
        "avif"
    ],
    "need_filter_image": false
}
ret = get_headers(c, i)
console.log(ret['X-s'].length)