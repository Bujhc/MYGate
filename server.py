from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # allow all origins for simplicity

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Handle drawing events from clients
@socketio.on('draw')
def handle_draw(data):
    # data contains x, y, color, thickness, etc.
    # Broadcast to all other clients except sender
    emit('draw', data, broadcast=True, include_self=False)



if __name__ == "__main__":

    socketio.run(app, host='0.0.0.0', port=5000)
    
