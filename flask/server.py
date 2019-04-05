from flask import Flask

app= Flask(__name__)

@app.route('/')

def index():
    return 'hello world'

# @app.route('/<user>')
# def user(user):
#     return "user %s" user

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return '<h1>HELLO %s</h1>' % username

app.run()