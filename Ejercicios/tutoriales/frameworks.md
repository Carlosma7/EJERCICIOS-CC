# Frameworks ASGI Python

Con el fin de estudiar diferentes frameworks tras la corrección, se han hecho una seria de ejemplos de prueba sencillos para poder trasladarlos al proyecto, los frameworks utilizados son:

* [Quart](https://pgjones.gitlab.io/quart/).
* [Starlette](https://www.starlette.io/).
* [FastAPI](https://fastapi.tiangolo.com/).
* [Sanic](https://sanic.readthedocs.io/en/latest/).
* [Vibora](https://vibora.io/).

El objetivo es realizar una demo sencilla en la que se reciba una petición post y se devuelva como resultado el mismo mensaje del post modificado.

### Quart

```python
from quart import Quart, Blueprint, jsonify, request
import json

# Definición de Blueprint
rutas_app = Blueprint("rutas_app", __name__)

@rutas_app.route('/', methods=['GET'])
async def test_function():
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener hello
	hello = data.get('hello')
	# Obtener world
	world = data.get('world')
	
	# Se añade el nombre al resultado
	resultado = hello + world + "Carlos."
	
	# Se devuelve el resultado
	return resultado, 200
```

### Starlette

```python
from starlette.applications import Starlette

# Definición de la aplicación
app = Starlette()

@app.route('/', methods=['GET'])
async def test_function(request):
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener hello
	hello = data.get('hello')
	# Obtener world
	world = data.get('world')
	
	# Se añade el nombre al resultado
	resultado = hello + world + "Carlos."
	
	# Se devuelve el resultado
	return resultado, 200

```

### FastAPI

```python
from fastapi import FastAPI
from pydantic import BaseModel

# Definición de la aplicación
app = FastAPI()

class Item(BaseModel):
    hello: str
    world: str

@app.get('/')
async def test_function(item: Item):	
	# Obtener hello
	hello = item.hello
	# Obtener world 
	world = item.world
	
	# Se añade el nombre al resultado
	resultado = hello + world + "Carlos."
	
	# Se devuelve el resultado
	return resultado, 200
```

### Sanic

```python
from sanic import Sanic, Blueprint
from sanic.response import json

# Definición de Blueprint
rutas_app = Blueprint("rutas_app", __name__)

@rutas_app.route('/', methods=['GET'])
async def test_function():
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener hello
	hello = data.get('hello')
	# Obtener world
	world = data.get('world')
	
	# Se añade el nombre al resultado
	resultado = hello + world + "Carlos."
	
	# Se devuelve el resultado
	return resultado, 200
```

### Vibora

```python
from vibora import Vibora, Blueprint

# Definición de Blueprint
rutas_app = Blueprint("rutas_app", __name__)

@rutas_app.route('/', methods=['GET'])
async def test_function():
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener hello
	hello = data.get('hello')
	# Obtener world
	world = data.get('world')
	
	# Se añade el nombre al resultado
	resultado = hello + world + "Carlos."
	
	# Se devuelve el resultado
	return resultado, 200
```

## Conclusiones finales

Como se puede observar, todas han sido implementaciones sencillas, y un punto de partida sobre el que trabajar en futuros desarrollos, de forma ampliable. Estos conocimientos se aplicarán directamente en el proyecto de la asignatura para poder decidir un framework adecuado para el mismo.
