# encoding: utf-8

# author: gendseo
# date: 2019-10-12

import requests
from bs4 import BeautifulSoup
from db import App, db

'''
    初始化全局变量
'''
base_url = 'https://www.coolapk.com'  # 主页
apk_url = base_url + '/apk'  # 应用页
apk_page_url = lambda p: base_url + '/apk?p=' + str(p)  # 第几页应用页


# 格式化下载量
# 万 => 乘以一万
# 亿 => 乘以一万再乘以一万
def format_downloads(d):
    w = 10000
    w_str = '万'
    y_str = '亿'
    d = str(d)
    # 判断万级别下载量
    if w_str in d:
        d = int(d.replace(w_str, '', -1))
        return d * w
    # 判断亿级别下载量
    elif y_str in d:
        d = int(d.replace(y_str, '', -1))
        return d * w * w
    else:
        return int(d)


# 页数范围是 1 到 get_pages()
def get_pages():
    r = requests.get(url=apk_url)
    rbs = BeautifulSoup(r.text, 'lxml')
    link = rbs.select('ul.pagination > li > a')[-1]
    return int(str(link['href']).split('=')[1])


# 获取当页的所有app
def get_page_apps(p=1):
    apps = []
    r = requests.get(url=apk_page_url(p))
    rbs = BeautifulSoup(r.text, 'lxml')
    links = rbs.select('div.app_left_list > a')
    for link in links:
        ts = str(link.select_one('p.list_app_info').text).split('\xa0')  # 混杂的数据
        # 名称
        name = str(link.select_one('p.list_app_title').text).strip()
        # 链接
        url = base_url + link['href']
        # 图片链接
        img = link.select_one('img')['src']
        # 评分
        score = ts[0].strip().replace('分', '', -1)
        # 大小
        size = ts[1].strip()
        # 下载量
        downloads = format_downloads(ts[2].strip().replace('次下载', '', -1))
        # 更新时间
        update = ts[3].strip().replace('更新', '', -1)
        # 简介
        description = str(link.select_one('p.list_app_description').text).strip()
        apps.append(
            App(name=name, url=url, img=img, score=score, size=size, downloads=downloads, update=update,
                description=description))
    return apps


# 运行爬虫，需要获取更多页请替换 range(x,y) 的 y 为 get_pages()
def run():
    db.drop_all()
    db.create_all()
    # pages = get_pages()
    # [x,y)
    for i in range(1, 11):
        a = get_page_apps(i)
        print(a)
        db.session.add_all(a)
        print('第 %d 页插入数据库成功' % i)
    db.session.commit()


if __name__ == '__main__':
    run()
