from flask import Flask,render_template
from flask_socketio import SocketIO,emit

app = Flask(__name__)
Socket = SocketIO(app)

@app.route('/')
def Index():
    return render_template('index.html')

@Socket.on('chat')
def Message(message):
    emit('new_message',message,broadcast=True)
    
    
@Socket.on('conn')
def Connect(user):
    emit('new_message',{'message' : f"{user} is connected!",'type' : 'conn'},broadcast=True)

if __name__ == '__main__':
    Socket.run(app,debug=True)