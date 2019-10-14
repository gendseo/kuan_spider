# encoding: utf-8
# author: gendseo
# date: 2019-10-12
# updated: 2019-10-14

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath('.')
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 错误追踪
# 使用轻量级的 SQLite3 测试
db_name = 'spider.db'  # 数据库名称
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + \
    str(basedir) + '/' + db_name
db = SQLAlchemy(app)


class App(db.Model):
    __tablename__ = 'app'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    url = db.Column(db.String(120))
    img = db.Column(db.String(120))
    version = db.Column(db.String(24))
    size = db.Column(db.String(24))
    download = db.Column(db.Integer)
    hot = db.Column(db.Integer)
    comment = db.Column(db.Integer)
    lang = db.Column(db.String(24))
    rank_num = db.Column(db.Float)
    rank_person = db.Column(db.Integer)
    pkg_name = db.Column(db.String(50))
    update = db.Column(db.String(50))
    rom = db.Column(db.String(50))
    author = db.Column(db.String(50))
    review = db.Column(db.String(200))

    def __init__(self, name, url, img, version, size, download, hot, comment, lang, rank_num, rank_person, pkg_name, update, rom, author, review):
        self.name = name
        self.url = url
        self.img = img
        self.version = version
        self.size = size
        self.download = download
        self.hot = hot
        self.comment = comment
        self.lang = lang
        self.rank_num = rank_num
        self.rank_person = rank_person
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
            'img': self.img,
            'version': self.version,
            'size': self.size,
            'download': self.download,
            'hot': self.hot,
            'comment': self.comment,
            'lang': self.lang,
            'rank_num': self.rank_num,
            'rank_person': self.rank_person,
            'pkg_name': self.pkg_name,
            'update': self.update,
            'rom': self.rom,
            'author': self.author,
            'review': self.review
        }
        return str(j)
