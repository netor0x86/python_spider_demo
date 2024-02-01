import requests
from bs4 import BeautifulSoup
import os

url = ''
main_url = url + '/book/sanguoyanyi.html'

headers = {  # 对爬虫的请求进行浏览器的伪装
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

path = './sanguo/'


def getPageText():
    response = requests.get(url=main_url, headers=headers)
    response.encoding = 'utf-8'
    # 3. 获取响应数据
    return response.text


def getDetailList(page_text):
    soup = BeautifulSoup(page_text, 'lxml')
    a_list = soup.select('.book-mulu > ul > li > a')
    return a_list


def saveContent(title, content):
    with open(path + title + '.txt', 'w') as fp:
        fp.write(content)

    print('==>> ', title, ' ::保存成功')


def getDetail(a_list):
    for a in a_list:
        title = a.string
        detail_url = url + a['href']

        detail_response = requests.get(url=detail_url, headers=headers)
        detail_response.encoding = 'utf-8'
        detail_page_text = detail_response.text

        soup_detail = BeautifulSoup(detail_page_text, 'lxml')

        detail_soup = soup_detail.find('div', class_='chapter_content')
        detail_text = detail_soup.text

        # 持久化存储
        saveContent(title, detail_text)


def main():
    if not os.path.exists(path):
        os.mkdir(path)

    page_text = getPageText()
    a_list = getDetailList(page_text)
    getDetail(a_list)


if __name__ == '__main__':
    main()
