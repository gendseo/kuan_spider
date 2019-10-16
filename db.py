# encoding: utf-8
# author: gendseo
# date: 2019-10-12
# updated: 2019-10-16

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

'''
    db 模块

    提供 orm 相关配置
    模型定义
    flask 实例
'''

basedir = os.path.abspath('.')
# flask 实例
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 错误追踪
# 使用轻量级的 SQLite3 测试
db_name = 'spider.db'  # 数据库名称
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + \
    str(basedir) + '/' + db_name  # 数据库地址
# orm 实例
db = SQLAlchemy(app)


class App(db.Model):
    # 序号
    id = db.Column(db.Integer, primary_key=True)
    # 名称，不能作为主键
    # 经测试，存在重复名称的 App
    name = db.Column(db.String(50))
    # 链接
    url = db.Column(db.String(120))
    # 版本
    version = db.Column(db.String(24))
    # 大小
    size = db.Column(db.String(24))
    # 下载量
    download = db.Column(db.Integer)
    # 关注数
    hot = db.Column(db.Integer)
    # 评论数
    comment = db.Column(db.Integer)
    # 语言
    lang = db.Column(db.String(24))
    # 评分
    rank = db.Column(db.Float)
    # 评分次数
    rank_num = db.Column(db.Integer)
    # 包名
    pkg_name = db.Column(db.String(50))
    # 更新时间
    update = db.Column(db.String(50))
    # ROM版本
    rom = db.Column(db.String(50))
    # 开发者
    author = db.Column(db.String(50))
    # 点评
    review = db.Column(db.String(200))

    def __init__(self, name, url, version, size, download, hot, comment, lang, rank, rank_num, pkg_name, update, rom, author, review):
        self.name = name
        self.url = url
        self.version = version
        self.size = size
        self.download = download
        self.hot = hot
        self.comment = comment
        self.lang = lang
        self.rank = rank
        self.rank_num = rank_num
        self.pkg_name = pkg_name
        self.update = update
        self.rom = rom
        self.author = author
        self.review = review

    def __repr__(self):
        j = {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'version': self.version,
            'size': self.size,
            'download': self.download,
            'hot': self.hot,
            'comment': self.comment,
            'lang': self.lang,
            'rank': self.rank,
            'rank_num': self.rank_num,
            'pkg_name': self.pkg_name,
            'update': self.update,
            'rom': self.rom,
            'author': self.author,
            'review': self.review
        }
        return str(j)
