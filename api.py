# encoding: utf-8

# author: gendseo
# date: 2019-10-12

from flask import render_template
from db import App, app
import service


@app.route('/')
def index():
    apps = App.query.order_by(App.score.desc(), App.downloads.desc()).all()
    return render_template('index.html', apps=apps)


@app.route('/score')
def score():
    all_score = [i[0] for i in App.query.with_entities(App.score).all()]
    return service.count_score(all_score)


if __name__ == '__main__':
    app.run()
