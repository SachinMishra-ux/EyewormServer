from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import secrets

app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = secrets.token_hex(16)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    # code to send the search term to the receiver device
    print(f"Received search term: {search_term}")
    socketio.emit('search_term', search_term, broadcast=True)
    return render_template('search.html', search_term=search_term)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)

