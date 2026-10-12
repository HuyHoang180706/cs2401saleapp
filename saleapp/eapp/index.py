from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    categories = [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 2,
        'name': 'Tablet'
    }, {
        'id': 3,
        'name': 'Laptop'
    }]

    return render_template('index.html', categories=categories)

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)