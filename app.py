from flask import Flask, request, jsonify

app = Flask(__name__)
latest_command = None

@app.route('/')
def index():
    return '<h1 style="color:red; background:black; text-align:center;">DSOTUM: Gölge Komut Merkezi</h1>'

@app.route('/shutdown', methods=['POST'])
def shutdown():
    global latest_command
    latest_command = 'shutdown'
    return 'Komut gönderildi', 200

@app.route('/command', methods=['GET'])
def get_command():
    global latest_command
    cmd = latest_command
    latest_command = None
    return jsonify({"cmd": cmd})
