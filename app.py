from flask import Flask, render_template
from flask_socketio import SocketIO, send
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '83fbefaebddbfa5c6230efaaf3762e27f3f4c02751bbc2c0c9ce3aa1011695cd'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Message received: {msg}")
    send(f"Server: {msg}", broadcast=True)  # Echo back the message to all clients

if __name__ == '__main__':
    if __name__ == '__main__':
        socketio.run(app)

