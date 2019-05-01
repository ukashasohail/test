from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello osama'

@app.route('/osama')
def hello1():
    return '<h1>hello from osama</h1>'

app.run()