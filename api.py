# encoding: utf-8
# author: gendseo
# date: 2019-10-12
# updated: 2019-10-16

from flask import render_template
from db import App, app
import service

'''
    api 模块

    提供可访问的 api 接口
'''


# 主页接口
# 返回主页模板
@app.route('/')
def index():
    apps = App.query.order_by(App.rank.desc(), App.rank_num.desc(
    ), App.hot.desc(), App.comment.desc()).all()
    return render_template('index.html', apps=apps)


# 评分统计接口
# 用于图表显示
@app.route('/count/ranks')
def ranks():
    ranks = [i[0] for i in App.query.with_entities(App.rank).all()]
    return service.count_rank(ranks)


# 评分和评分次数关系统计接口
# 用于图表显示
@app.route('/count/rank_rank_num')
def ranks_rank_num():
    apps = App.query.order_by(App.rank.desc(), App.rank_num.desc(), App.hot.desc(
    ), App.comment.desc()).with_entities(App.name, App.rank_num, App.rank).all()
    return {'data': [i[1:] for i in apps], 'name': [i[0] for i in apps]}


if __name__ == '__main__':
    app.run(debug=True)
