# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import sys
sys.path.append('..')  # Thêm thư mục cha vào sys.path

from LogisticRegression.chat_using_LogisticRegression import chat_bot_LR

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('html/index.html')

@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    emit('message', chat_bot_LR(message))

if __name__ == '__main__':
    socketio.run(app)