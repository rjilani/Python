__author__ = 'rjilani'

from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    a = 5
    return '<h1><b>Rashid jilani</b></h1>'

if __name__ == '__main__':
    app.run(debug=True)