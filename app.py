from flask import Flask, request, jsonify
import json

app = Flask(__name__)

input = open('cleaned_new.json')
data = json.load(input)

@app.route('/')
def index():
	return 'Hey! It works.'

@app.route('/<string:com_name>', methods=['GET'])
def get_commodity(com_name):
	return jsonify({com_name: data[com_name]})


if __name__ == '__main__':
    app.run(debug=True)