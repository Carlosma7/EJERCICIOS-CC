from flask import Flask, jsonify, request
import json
app2 = Flask(__name__)

def set_routes(app2):
	@app2.route('/api/fruits')
	def get_frutas():
		apple = json.dumps({"name": "Apple", "color": "Red", "family": "Acid"})
		avocado = json.dumps({"name": "Avocado", "color": "Green", "family": "Neutral"})
		pear = json.dumps({"name": "Pear", "color": "Green", "family": "Sweet"})

		return jsonify([apple, avocado, pear]), 200
	
	@app2.route('/api/insert', methods=['POST'])
	def insert_fruit():
		data_string = request.get_data()
		data = json.loads(data_string)
		
		fruit_name = data.get('name')
		fruit_color = data.get('color')
		fruit_family = data.get('family')

		if fruit_name and fruit_color and fruit_family:
			return 'Ok', 200
		else:
			return 'Error', 400

if __name__ == '__main__':
    app2.run()

