from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shop-by-occasion')
def shop_by_occasion():
    return render_template('shop_by_occasion.html')
