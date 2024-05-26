import requests
import execjs
import urllib.parse

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'ttwid=1%7CduF4xl-WsG7zTxGUCFDXbLIVrsRzcj5IsMH_PY4A5ds%7C1715643814%7C2803fc5f8b785564234a9433956a1ce64dab027ce880992b98c37a4de3e94619; s_v_web_id=verify_lw5m1f2a_4krOOsDT_Ngb7_464c_BIEf_XR5oqdNuDhZO; __ac_nonce=0664fd5b5000e5a9ff853; __ac_signature=_02B4Z6wo00f01nvO5rgAAIDDlesiRyUEqdp77uIAAPjLcd; douyin.com; device_web_cpu_core=4; device_web_memory_size=8; dy_swidth=1920; dy_sheight=1080; csrf_session_id=ca9dbb7caeae09b371d0619feb0c1df4; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; strategyABtestKey=%221716508091.853%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; passport_csrf_token=e4e6d822e28f54a43b135d451f6685f3; passport_csrf_token_default=e4e6d822e28f54a43b135d451f6685f3; xgplayer_user_id=694554036205; bd_ticket_guard_client_web_domain=2; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; xg_device_score=6.94375426938166; SEARCH_RESULT_LIST_TYPE=%22single%22; pwa2=%220%7C0%7C1%7C0%22; download_guide=%222%2F20240524%2F0%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSTNaV1JwTDhuNHhuWmd0MUdIWmI3L25rQkVJU0NHQ2ZsL1gxcmRhRGlxYTVVNjFMcDNQUmcwL1liMTFHUnRJWTMvREpCZ2dxeUQ4WUwyVzBkcWtkdmc9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=gC44_BEmJMIXGa30QQbZkez867mEBlbz5bGVgVLG5_5ulKx5H7D6QAH1gtyqGJKOrR_Yfvuwnb7E8_WF0zcQwxNIPFfwR5NogRhI4jsELJCsZcRcoWa6XGg1pECHSg==; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAAQERLUS1XLl1qZMZDkibRWUdHGBAoG0pJq_5hAj3XjIZXnxgtW_CcE17nuHHfikpQ',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

params = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'sec_user_id': 'MS4wLjABAAAAQERLUS1XLl1qZMZDkibRWUdHGBAoG0pJq_5hAj3XjIZXnxgtW_CcE17nuHHfikpQ',
    # 'sec_user_id': 'MS4wLjABAAAAMbqnWxzUfZegt9vrNBDz7zyqwhvG6vXiKTDxVm2wUD0',
    'max_cursor': '0',
    'locate_query': 'false',
    'show_live_replay_strategy': '1',
    'need_time_list': '1',
    'time_list_query': '0',
    'whale_cut_token': '',
    'cut_version': '1',
    'count': '18',
    'publish_video_strategy_type': '2',
    'update_version_code': '170400',
    'pc_client_type': '1',
    'version_code': '290100',
    'version_name': '29.1.0',
    'cookie_enabled': 'true',
    'screen_width': '1920',
    'screen_height': '1080',
    'browser_language': 'zh-CN',
    'browser_platform': 'MacIntel',
    'browser_name': 'Chrome',
    'browser_version': '124.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '124.0.0.0',
    'os_name': 'Mac OS',
    'os_version': '10.15.7',
    'cpu_core_num': '4',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '10',
    'effective_type': '4g',
    'round_trip_time': '50',
    'webid': '7368633937193813504',
    'verifyFp': 'verify_lw5m1f2a_4krOOsDT_Ngb7_464c_BIEf_XR5oqdNuDhZO',
    'fp': 'verify_lw5m1f2a_4krOOsDT_Ngb7_464c_BIEf_XR5oqdNuDhZO',
    'msToken': 'maudhvGpKKMHsM_VX0AW2I6Zgvj9s8IUjpuhKUqR76kFSoFmSpcjCVqahStUx-0nDxpGnYRb8rJCe2trR5prenEHVfCpa1r44jphuXhp4j0wszPoN5B0YyBtH_3k_Q==',
    # 'a_bogus': 'OfRMQdzvDk6NkfWf5V/LfY3q61q3YM/K0trEMD2fanfVnL39HMOu9exL8m4vDxLjLG/lIeDjy4hbYNCDrQQy81wfHuXi/2AdQfSZeMVQ524j5Hk7uy68nTJx4vJlFel057NAxc40y75azYT0AooH-iI4Ofoja3Lk96Et7pZTRpS/xKTV',
}

with open('./dy.js', 'r') as fp:
    js_code = fp.read()

js_engine = execjs.compile(js_code)
ret = js_engine.call('get_a_b', urllib.parse.urlencode(params))
print(ret)
params['a_bogus'] = ret

response = requests.get('https://www.douyin.com/aweme/v1/web/aweme/post/', params=params, headers=headers)
print(response.text)
