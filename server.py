from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Store connected clients
clients = {}


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def handle_connect():
    clients[request.sid] = request.namespace


@socketio.on('disconnect')
def handle_disconnect():
    clients.pop(request.sid)


@socketio.on('message')
def handle_message(data):
    sender = request.sid
    recipient = data['recipient']
    message = data['message']

    # Perform encryption, message handling, etc.
    # You can relay the message to the recipient or store it in a database, depending on your needs.

    # Send the message to the recipient
    if recipient in clients:
        emit('message', {'sender': sender, 'message': message}, room=clients[recipient].sid)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
