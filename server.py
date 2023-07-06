from flask import Flask, request

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def receive_message():
    message = request.form.get('message')
    # Handle the received message, perform encryption, etc.
    # You can store the messages in a database, relay them to other clients, etc.
    return 'Message received'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
