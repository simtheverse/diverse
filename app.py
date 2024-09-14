from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit
import logging

app = Flask(__name__)
socketio = SocketIO(app)

people = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getPeople', methods=['GET'])
def get_people():
    return jsonify(people)

@app.route('/addPerson', methods=['POST'])
def add_person():
    person_data = request.json
    people.append(person_data)
    logging.info(f'Emitting update_people event with data: {people}')
    socketio.emit('update_people', people)
    return jsonify({'status': 'success', 'person': person_data})

@socketio.on('connect')
def handle_connect():
    logging.info('Client connected')
    emit('update_people', people)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    socketio.run(app, debug=True)