# encoding: utf-8
# author: gendseo
# date: 2019-10-12
# updated: 2019-10-14

import requests
from bs4 import BeautifulSoup
from db import App, db
import re
import json

'''
    初始化全局变量
'''
base_url = 'https://www.coolapk.com'  # 主页
apk_url = base_url + '/apk'  # 应用页


def apk_page_url(p): return base_url + '/apk?p=' + str(p)  # 第几页应用页


# 格式化数值
# 万 => 乘以一万
# 亿 => 乘以一万再乘以一万
def format_size(d):
    w = 10000
    w_str = '万'
    y_str = '亿'
    d = str(d)
    # 判断万级别
    if w_str in d:
        d = float(d.replace(w_str, '', -1))
        return int(d * w)
    # 判断亿级别
    elif y_str in d:
        d = float(d.replace(y_str, '', -1))
        return int(d * w * w)
    else:
        return int(d)


# 进一步到 APP 详情页获取更详细的数据
def get_app_info(url):
    _r = requests.get(url=url)
    _rbs = BeautifulSoup(_r.text, 'lxml')
    # 图标
    _img = str(_rbs.select_one('div.apk_topbar > img')['src'])
    # 版本
    _version = str(_rbs.select_one(
        'p.detail_app_title > span.list_app_info').text).strip()
    # 混杂的数据
    _ts = str(_rbs.select_one('p.apk_topba_message').text).split('/')
    # 大小
    _size = str(_ts[0]).strip()
    # 下载量
    _download = format_size(str(_ts[1]).strip().replace('下载', '', -1))
    # 关注量
    _hot = format_size(str(_ts[2]).strip().replace('人关注', '', -1))
    # 评论数
    _comment = format_size(str(_ts[3]).strip().replace('个评论', '', -1))
    # 语言
    _lang = str(_ts[4]).strip()
    # 评论分
    _rank_num = str(_rbs.select_one('div.apk_rank > p.rank_num').text)
    # 评论数
    _rank_person = format_size(str(re.findall(re.compile(r'共(.*?)个评分', re.S), str(
        _rbs.select_one('div.apk_rank > div.rank_star > p.apk_rank_p1').text))[0]))
    # 混杂的数据
    _ts = [str(i.strip()) for i in str(_rbs.select('div.apk_left_title')
                                    [-2].select_one('p.apk_left_title_info').text).split('\n')]
    # 应用包名
    _pkg_name = _ts[0].replace('应用包名：', '', -1)
    # 更新时间
    _update = _ts[1].replace('更新时间：', '', -1)
    # 支持系统
    _rom = _ts[2].replace('支持ROM：', '', -1)
    # 开发者名称
    _author = _ts[3].replace('开发者名称：', '', -1)
    return {'img': _img, 'version': _version, 'size': _size, 'download': _download, 'hot': _hot, 'comment': _comment,
            'lang': _lang, 'rank_num': _rank_num, 'rank_person': _rank_person, 'pkg_name': _pkg_name, 'update': _update, 'rom': _rom, 'author': _author}


# 页数范围是 1 到 get_pages()
def get_pages():
    r = requests.get(url=apk_url)
    rbs = BeautifulSoup(r.text, 'lxml')
    link = rbs.select('ul.pagination > li > a')[-1]
    return float(str(link['href']).split('=')[1])


# 获取当页的所有app
def get_page_apps(p=1):
    _apps = []
    _r = requests.get(url=apk_page_url(p))
    _rbs = BeautifulSoup(_r.text, 'lxml')
    _links = _rbs.select('div.app_left_list > a')
    for _link in _links:
        # 链接
        _url = base_url + _link['href']
        # 至于为什么在这里获取这几个数据是因为app详情页里有很多歧义数据，会使爬虫解析出现错误
        # 名称
        _name = str(_link.select_one('p.list_app_title').text).strip()
        # 点评
        _review = str(_link.select_one('p.list_app_description').text).strip()
        _app_info = get_app_info(_url)
        _apps.append(App(name=_name, url=_url, img=_app_info['img'], version=_app_info['version'], size=_app_info['size'], download=_app_info['download'],
                        hot=_app_info['hot'], comment=_app_info['comment'], lang=_app_info[
            'lang'], rank_num=_app_info['rank_num'], rank_person=_app_info['rank_person'],
            pkg_name=_app_info['pkg_name'], update=_app_info['update'], rom=_app_info['rom'], author=_app_info['author'], review=_review))
    return _apps


# 运行爬虫，需要获取更多页请替换 range(x,y) 的 y 为 get_pages()
def run():
    db.drop_all()
    db.create_all()
    # y = get_pages()
    y = 11
    # [x,y)
    for i in range(1, y):
        db.session.add_all(get_page_apps(i))
        print('%s\n第 %d 页数据获取成功' % ('*' * 50, i))
        if i == y - 1:
            db.session.commit()
            print('全部页的数据存入数据库成功')
            break
        if i % 5 == 0:
            db.session.commit()
            print('%s\n前 %d 页数据存入数据库成功' % ('-' * 50, i))


if __name__ == '__main__':
    run()
