from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)


message_id_counter = 0

@app.route('/')
def index():
    return render_template('WebSocketClient.html')


@socketio.on('join')
def handle_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send({'username': 'System', 'message': f'{username} has joined the room.'}, to=room)


@socketio.on('message')
def handle_message(data):
    global message_id_counter
    username = data['username']
    message = data['message']
    room = data.get('room')
    
    message_id_counter += 1  
    send({'id': message_id_counter, 'username': username, 'message': message}, to=room)


@socketio.on('edit_message')
def handle_edit_message(data):
    room = data['room']
    send({'id': data['id'], 'username': data['username'], 'message': data['message']}, to=room)


@socketio.on('delete_message')
def handle_delete_message(data):
    room = data['room']
   
    send({'id': data['id']}, to=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
