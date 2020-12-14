from flask import Flask
import json
import pytest

from app2 import set_routes

# Test que comprueba que existe una fruta roja
def test_one_red_fruit():
    app = Flask(__name__)
    set_routes(app)
    client = app.test_client()
    url = '/api/fruits'

    response = client.get(url)
    
    # Assert status code Ok
    assert response.status_code == 200
    
    fruits = response.get_data()
    fruits = json.loads(fruits)
    # Assert there is a red fruit
    assert 'Red' in [json.loads(fruit)['color'] for fruit in fruits]

# Test que se inserta una nueva fruta con el formato correcto
def test_new_fruit():
	app = Flask(__name__)
	set_routes(app)
	client = app.test_client()
	url = '/api/insert'
	
	new_fruit = {
		'name': 'Banana',
		'color': 'Yellow',
		'family': 'Sweet'
	}
	
	response = client.post(url, data = json.dumps(new_fruit))
	assert response.status_code == 200
