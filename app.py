from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

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
    return jsonify({'status': 'success', 'person': person_data})

if __name__ == '__main__':
    app.run(debug=True)