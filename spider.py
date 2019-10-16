# encoding: utf-8
# author: gendseo
# date: 2019-10-12
# updated: 2019-10-16

import requests
from bs4 import BeautifulSoup
import time
import os

from db import App, db
import re

'''
    spider 模块

    提供一个爬虫主体，使数据填充数据库。
'''

'''
    初始化全局变量
'''
_base_url = 'https://www.coolapk.com'  # 主页
_apk_url = _base_url + '/apk'  # 应用页


def _apk_page_url(p): return _base_url + '/apk?p=' + str(p)  # 第几页应用页


# 格式化数值
# 万 => 乘以一万
# 亿 => 乘以一万再乘以一万
def _format_size(d):
    _w = 10000
    _w_str = '万'
    _y_str = '亿'
    _d = str(d)
    # 判断万级别
    if _w_str in _d:
        _d = float(_d.replace(_w_str, '', -1))
        return int(_d * _w)
    # 判断亿级别
    elif _y_str in _d:
        _d = float(_d.replace(_y_str, '', -1))
        return int(_d * _w * _w)
    # 无关键字，返回该数
    else:
        return int(_d)


# 根据 url 发起请求获取内容
def _get_html(url):
    try:
        _r = requests.get(url=url)
        _rbs = BeautifulSoup(_r.text, 'lxml')
        _r.close()
        return _rbs
    except Exception as e:
        print(e)
        return


# 进一步到 APP 详情页获取更详细的数据
def get_app_info(url):
    _rbs = _get_html(url=url)
    # 版本
    _version = str(_rbs.select_one('p.detail_app_title > span.list_app_info').text).strip()
    # 混杂的数据
    _ts = str(_rbs.select_one('p.apk_topba_message').text).split('/')
    # 大小
    _size = str(_ts[0]).strip()
    # 下载量
    _download = _format_size(str(_ts[1]).strip().replace('下载', '', -1))
    # 关注量
    _hot = _format_size(str(_ts[2]).strip().replace('人关注', '', -1))
    # 评论数
    _comment = _format_size(str(_ts[3]).strip().replace('个评论', '', -1))
    # 语言
    _lang = str(_ts[4]).strip()
    # 评分
    _rank = str(_rbs.select_one('div.apk_rank > p.rank_num').text)
    # 评分次数
    _rank_num = _format_size(str(re.findall(re.compile(r'共(.*?)个评分', re.S), str(_rbs.select_one('div.apk_rank > div.rank_star > p.apk_rank_p1').text))[0]))
    # 混杂的数据
    _ts = [str(i.strip()) for i in str(_rbs.select('div.apk_left_title')[-2].select_one('p.apk_left_title_info').text).split('\n')]
    # 应用包名
    _pkg_name = _ts[0].replace('应用包名：', '', -1)
    # 更新时间
    _update = _ts[1].replace('更新时间：', '', -1)
    # 支持系统
    _rom = _ts[2].replace('支持ROM：', '', -1)
    # 开发者名称
    _author = _ts[3].replace('开发者名称：', '', -1)
    # 返回一个字典，方便调用的函数通过 key 获取 value
    return {'version': _version, 'size': _size, 'download': _download, 'hot': _hot, 'comment': _comment,
            'lang': _lang, 'rank': _rank, 'rank_num': _rank_num, 'pkg_name': _pkg_name, 'update': _update, 'rom': _rom,
            'author': _author}


# 保存图片到项目的 icon 目录
def _get_img(url, name):
    # 构造目录地址
    _dirname = os.path.abspath('.') + '/static/icon/'
    # 检查目录地址，不存在就创建
    if not os.path.exists(_dirname):
        os.mkdir(_dirname)
    # 拼接图片名
    _name = str(name) + '.png'
    # 拼接完整图片路径
    _filename = str(_dirname + _name)
    if os.path.exists(_filename):
        print(name, end=' ')
        return
    # 下载并保存
    _r = requests.get(url=url)
    with open(_filename, 'wb') as f:
        f.write(_r.content)
        print(name, end=' ')
    _r.close()


# 页数范围是 1 到 _get_pages()
def _get_pages():
    _rbs = _get_html(url=_apk_url)
    _link = _rbs.select('ul.pagination > li > a')[-1]
    return int(str(_link['href']).split('=')[1])


# 获取当页的所有app
def _get_page_apps(p=1):
    _apps = []
    _rbs = _get_html(url=_apk_page_url(p))
    # _links 里是当页的所有 APP 的 a 标签
    _links = _rbs.select('div.app_left_list > a')
    print('第', end=' ')
    for _i, _link in enumerate(_links):
        # 图片
        _img = str(_link.select_one('img.alllist_img')['src'])
        _get_img(url=_img, name=((_i + 1) + ((p - 1) * 10)))
        # 链接
        _url = _base_url + _link['href']
        _app_info = get_app_info(_url)
        # 至于为什么在这里获取这几个数据是因为app详情页里有很多歧义数据，会使爬虫解析出现错误
        # 名称
        _name = str(_link.select_one('p.list_app_title').text).strip()
        # 点评
        _review = str(_link.select_one('p.list_app_description').text).strip()
        # 将 App 对象添加到列表中，方便 orm 一次性提交
        _apps.append(App(name=_name, url=_url, version=_app_info['version'], size=_app_info['size'], download=_app_info['download'],
                        hot=_app_info['hot'], comment=_app_info['comment'], lang=_app_info['lang'], rank=_app_info['rank'],
                        rank_num=_app_info['rank_num'],pkg_name=_app_info['pkg_name'], update=_app_info['update'], rom=_app_info['rom'],
                        author=_app_info['author'], review=_review))
    print('张图片保存成功')
    return _apps


# 如果需要续点传送请手动控制[x,y)的值
# 运行爬虫，需要获取更多页请替换 range(x,y) 的 y 为 get_pages()
def run():
    db.drop_all()  # 删除数据库
    db.create_all()  # 创建数据库
    # [x,y) 页
    x = 1
    y = 10  # 10 '前十页' | _get_pages() '所有页'
    for i in range(x, y + 1):
        # 一次性提交该页的所有 App
        db.session.add_all(_get_page_apps(i))
        print('第 %d 页数据获取成功' % i)
        if i == y:
            # 提交事务
            db.session.commit()
            print('%s\n全部页的数据存入数据库成功' % ('*' * 30))
            break
        if i % 5 == 0:
            # 提交事务
            db.session.commit()
            # time.sleep(1)
            print('%s\n前 %d 页数据存入数据库成功\n爬虫暂停 1s\n%s' % ('-' * 30, i, '-' * 30))


# 爬虫主体入口
if __name__ == '__main__':
    run()
