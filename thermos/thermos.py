from datetime import datetime
from os import urandom
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
bookmarks = []
app.config['SECRET_KEY'] = urandom(24)
#app.config['SECRET_KEY'] = b'\xae\x87\xa0\xbd\xfbm\x18L\x9aH\x1d\xe7\xe1\xbd\xe1/\xd4\xc3B\x15\xd06\x88\xda'

def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = "maros",
        date = datetime.utcnow()
    ))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        flash("Stored bookmark  '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
