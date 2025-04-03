import os
from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():
    return "SocketIO server is running on Render!"

@socketio.on('message')
def handle_message(msg):
    print(f"Received: {msg}")
    emit('message', f"Echo: {msg}", broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render sets PORT env var
    socketio.run(app, host='0.0.0.0', port=port)
