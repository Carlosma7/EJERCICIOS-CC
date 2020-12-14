from flask import Flask, jsonify
import json
app1 = Flask(__name__)


@app1.route('/api/fruits')
def get_frutas():
	apple = json.dumps({"name": "Apple", "color": "Red", "family": "Acid"})
	avocado = json.dumps({"name": "Avocado", "color": "Green", "family": "Neutral"})
	pear = json.dumps({"name": "Pear", "color": "Green", "family": "Sweet"})

	return jsonify([apple, avocado, pear]), 200

if __name__ == '__main__':
    app1.run()

