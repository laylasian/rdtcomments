from flask import Flask, url_for, jsonify
import json
app = Flask(__name__)

@app.route('/')
def api_root():
	with open('2015_01.json') as data_file:    
		data = json.load(data_file)
	return jsonify(data[2])

@app.route('/ohai')
def api_ohai():
	return 'ohai! ????'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)