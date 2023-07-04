from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.json.get('message')
    encrypted_message = encrypt(message)  # Implement your encryption logic here
    return jsonify({'encrypted_message': encrypted_message}), 200

@app.route('/receive_message', methods=['GET'])
def receive_message():
    encrypted_message = request.args.get('encrypted_message')
    decrypted_message = decrypt(encrypted_message)  # Implement your decryption logic here
    return jsonify({'decrypted_message': decrypted_message}), 200

def encrypt(message):
    # Implement your encryption logic here
    return message[::-1]

def decrypt(encrypted_message):
    # Implement your decryption logic here
    return encrypted_message[::-1]

if __name__ == '__main__':
    app.run(host='0.0.0.0')
