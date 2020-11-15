from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good</h2>'

@app.route('/profile/<username>')
def profile(username):
    return 'Hey there %s' % username

if __name__ == "__main__":
    app.run(debug = True)
