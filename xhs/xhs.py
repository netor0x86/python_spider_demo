import requests
import json
import execjs

cookies = {
    'abRequestId': '20a5f287-8aca-5bab-9fdf-45cfb94cff09',
    'a1': '18aa656343584vnxom74uo55f3zeucvkcemzlytdy30000269770',
    'webId': '5764d58efe63dd43d91b4b0795425628',
    'gid': 'yY00K2KqjjSjyY00K2Kq4dv9q2Y4hICl6W476fvl22iquuq8d7ShT1888JKjWW88iYSifdfS',
    'web_session': '030037a23490533fc2d07f843d224a488e882c',
    'xsecappid': 'xhs-pc-web',
    'webBuild': '4.16.0',
    'acw_tc': '7ff0e5267e7b60c9192b16c130e0624f0901d8236b147dc48e0853a47882a3cf',
    'websectiga': '16f444b9ff5e3d7e258b5f7674489196303a0b160e16647c6c2b4dcb609f4134',
    'sec_poison_id': 'b560ffe1-62bc-48ed-98d7-0b1926f1f90d',
    'unread': '{%22ub%22:%2266442062000000001e020fd3%22%2C%22ue%22:%2266246f60000000001c00959c%22%2C%22uc%22:25}',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'abRequestId=e9ffb6a7-e66e-543c-a581-133cb3a0aea1; webBuild=4.16.1; a1=18f9d69453fjjzj01y7pbyp9zk64n5t11mbb6tr3v30000429062; webId=63fe2c7e0e3aeb8aae5397bd580da405; acw_tc=57fe994e260ccffb4971916c39dcaa3e87b0e4aa6bc6c16f2dca1280673734f0; websectiga=3633fe24d49c7dd0eb923edc8205740f10fdb18b25d424d2a2322c6196d2a4ad; sec_poison_id=cb3ec16b-a177-42fb-aa34-0d1082662692; web_session=030037a17e7d3e0bf478066f35214a2cee59c8; gid=yYijfKj4SiyiyYijfKj4269FqiVVuV8yvWUDDqhvUjuTKDq84I29yK8884Jj8KJ8SjdDqWJ0; unread={%22ub%22:%2266400a72000000001e0381b3%22%2C%22ue%22:%22662c79d300000000010076c3%22%2C%22uc%22:29}; xsecappid=xhs-pc-web',
    'origin': 'https://www.xiaohongshu.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-b3-traceid': 'ccc78962994edf5b',
    'x-s-common': '2UQAPsHCPUIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1+jhhHjIj2eHjwjQ+GnPW/MPjNsQhPUHCHdYiqUMIGUM78nHjNsQh+sHCH0c1P/G1PaHVHdWMH0ijP/Yfwnc9w/cMP98xydkxPebE+7mj2gZE2fV9+BhM4erlJnQj+dzUP7GAPeZIPecUw/Z9PjHVHdW9H0il+Ar9PAPUweD7Per7NsQh+UHCHSY8pMRS2LkCGp4D4pLAndpQyfRk/SzbyLleadkYp9zMpDYV4Mk/a/8QJf4hanS7ypSGcd4/pMbk/9St+BbH/gz0zFMF8eQnyLSk49S0Pfl1GflyJB+1/dmjP0zk/9SQ2rSk49S0zFGMGDqEybkea/8QyDDA/nknyDELc/pOpFph/pztyFECGAzOzBqF/F4p2DFUz/bOpBVF/F4p+rMxp/+wyDEk/Fzp2LMo//byzM8k/Fz+2DMxcfY8JLFA/M482SSxafSwPSp7/fkm2SSTn/QwzbDI/F4Q+rRrG7kypb8knpzsJLEL/fMwPSrMnD4Q+bDU//pyprEknfMayrMgnfY8pr8Vnnk34MkrGAm8pFpC/p4QPLEo//++JLE3/L4zPFEozfY+2D8k/SzayDECafkyzF8x/Dzd+pSxJBT8pBYxnSznJrEryBMwzF8TnnkVybDUnfk+PS8i/nkyJpkLcfS+ySDUnpzyyLEo/fk+PDEk/Sz3+LFUL/bOzbpE/nkQ+rMxn/z+zFkV/fkz2LFUL/z+2DbC/LzDyrRLp/bw2SpCnpzyJrELafY+Jpk3nfM+2DMCpfMyzrDF/gkb4FExGAmOzrMhnD4yyrRrn/mw2DDInnk3PbSCJBMyprbC/L4QPrExafk8PDkx/pz8+bSgz/QOzrkknDz+2LELy7YOzbLF/Dzd+LMLcfYOzbQT/FzmPSSL8AmwpbLMnSz3Ppkxn/pwPDDM/L4pPpkTn/pOzrrInDzBypkLng4+pB+C/Mz8+bSLpfT82SQTngk02LErLg4w2SLM/F4yyFEC/gSwpbLMnD4wJbSgng4+yfY3/fMByrMea0DjNsQhwsHCHDDAwoQH8B4AyfRI8FS98g+Dpd4daLP3JFSb/BMsn0pSPM87nrldzSzQ2bPAGdb7zgQB8nph8emSy9E0cgk+zSS1qgzianYt8LcE/LzN4gzaa/+NqMS6qS4HLozoqfQnPbZEp98QyaRSp9P98pSl4oSzcgmca/P78nTTL0bz/sVManD9q9z1J9p/8db8aob7JeQl4epsPrz6ag8+2DRyLgbypdq7agYO8pzl47HFqgzkanTU/FSkN7+3G9+haL+P8rDA/9LI4gzVPDbrnd+P4fprLFTALMm7+LSb4d+k4gzt/7b7wrQn498cqBzSprzg/FSh+b8QygL9nSm7GSmM4epQ4flY/BQdqA+l4oYQ2BpAPp87arS34nMQyFSE8nkdqMD6pMzd8/4AydpFa7Qy89pDpFDE898N8pS8qnEQP94A8S8FJDSb8npx4gz9JgkkPLE6zrEQP9zSpopFLUR/a9L9JAzcanYjqFSbzo4zpL48a/+CqpbgweYQygkMcS87cLS9zFGFcfzAnpkSqA8n4M8Q4DbS8B8N8pD6LfEQynzSPgQyP7SM4BSQy9RAP/49q9T8N7+k4g408/qMqM+c4bzQPM8jnfq9qM4c4rpC89zApM8FtFDAy9+Q2BMDq7bFqnRl4Bp18F8jqgQO8pSx87+h4gzdanTD8pSY+gP9GDD9anTOq9kr4d+3cDlBanTO8pzn4bSQygQ34opFJgzM4o8Q2BpSpbmFzDSb+fLA4gzBanTd8nzl4bQ0pdzmqSmFpLDALd8Q4S8l4BzQLDkP4fLALozQaLprGLS3PBp84g4znfQb+rIIPo+x8pbManTg/o4l4rYy4gqAag868/8n4FE1LFTA+SqROaHVHdWEH0iA+0rFPAH9PAHVHdWlPsHCPAzR',
}

json_data = {
    'cursor_score': '',
    'num': 31,
    'refresh_type': 1,
    'note_index': 35,
    'unread_begin_note_id': '',
    'unread_end_note_id': '',
    'unread_note_count': 0,
    'category': 'homefeed.food_v3',
    'search_key': '',
    'need_num': 6,
    'image_formats': [
        'jpg',
        'webp',
        'avif',
    ],
    'need_filter_image': False,
}

add_headers = execjs.compile(open('xhs.js').read()).call('get_headers', '/api/sns/web/v1/homefeed', json_data)
headers['x-s'] = add_headers['X-s']
headers['x-t'] = str(add_headers['X-t'])
# print(len(headers['x-s']))
# print(headers['x-s'])
data = json.dumps(json_data, separators=(",", ":"))
# response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/homefeed', cookies=cookies, headers=headers,
#                          json=json_data)
response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/homefeed', cookies=cookies, headers=headers,
                         data=data)
print(response.text)
