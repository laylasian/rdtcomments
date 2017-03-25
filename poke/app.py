from flask import Flask, url_for, jsonify
import json
app = Flask(__name__)

@app.route('/')
def api_root():
	return 'OHAI =^_^='

@app.route('/comments')
def api_comments():
	with open('2015_01.json') as data_file:    
		data = json.load(data_file)
	return jsonify(data)
	#return jsonify(data["comments"])

@app.route('/comment/<int:comment_id>')
def api_comment(comment_id):
	with open('2015_01.json') as data_file:    
		data = json.load(data_file)
	return jsonify(data["comments"][comment_id])

@app.route('/test')
def api_blargh():
	with open('2015_01.json') as data_file:    
		data = json.load(data_file)
		w = data["comments"]
		t = w[2]
	return t["body"]

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)