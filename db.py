# encoding: utf-8

# author: gendseo
# date: 2019-10-12

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath('.')
app = Flask(__name__)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # 自动提交事务
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 链路追踪
# 使用轻量级的 SQLite3 测试
db_name = 'test.db'  # 数据库名称
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + str(basedir) + '/' + db_name
db = SQLAlchemy(app)


class App(db.Model):
    __tablename__ = 'app'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    url = db.Column(db.String(120))
    img = db.Column(db.String(120))
    score = db.Column(db.Float)
    size = db.Column(db.String(24))
    downloads = db.Column(db.Integer)
    update = db.Column(db.String(50))
    description = db.Column(db.String(200))

    def __init__(self, name, url, img, score, size, downloads, update, description):
        self.name = name
        self.url = url
        self.img = img
        self.score = score
        self.size = size
        self.downloads = downloads
        self.update = update
        self.description = description

    def __repr__(self):
        j = {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'img': self.img,
            'score': self.score,
            'size': self.size,
            'downloads': self.downloads,
            'update': self.update,
            'description': self.description,
        }
        return str(j)
