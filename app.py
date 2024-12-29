from flask import Flask, render_template, request, url_for
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    socketio.run(app, debug=True)