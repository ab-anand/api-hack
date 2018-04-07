from flask import Flask, request, jsonify
import json, os

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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
