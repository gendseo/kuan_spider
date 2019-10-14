# encoding: utf-8
# author: gendseo
# date: 2019-10-12
# updated: 2019-10-14

from flask import render_template
from db import App, app
import service


@app.route('/')
def index():
    apps = App.query.order_by(App.rank_num.desc(), App.hot.desc(), App.comment.desc()).all()
    return render_template('index.html', apps=apps)


@app.route('/score')
def score():
    all_rank_num = [i[0] for i in App.query.with_entities(App.rank_num).all()]
    return service.count_rank_num(all_rank_num)


if __name__ == '__main__':
    app.run(debug=True)
