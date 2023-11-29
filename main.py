from flask import Flask, request, jsonify
from service.databaseConnect import getAllRecordsFrmDb

app = Flask(__name__)


@app.route('/show', methods=['GET'])
def show():
    sen = getAllRecordsFrmDb()
    return sen


@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if not first_name or not last_name:
        return jsonify({'error': 'Please provide both first name and last name'}), 400

    greeting = f"Hello, {first_name} {last_name}! Welcome to the API."
    return jsonify({'greeting': greeting})


if __name__ == '__main__':
    app.run(debug=True)
