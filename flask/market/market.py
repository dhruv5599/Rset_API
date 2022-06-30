from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')



# this fir market page
@app.route('/market')
def market_page():
        items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150},
        {'id': 4, 'name': 'mice', 'barcode': '231985128466', 'price': 500},
        {'id': 5, 'name': 'mouse', 'barcode': '231985129446', 'price': 650},

    ]
        return render_template('market.html', items=items)

# parameters is work as it is like inheritance
# we can use this for primary key or filtering
@app.route('/about/<name>')
def about_page(name):
    return f'this is about page {name}'