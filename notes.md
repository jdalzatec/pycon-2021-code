pipenv shell
pip install chalice
chalice new-project to-do
se crea un folder to-do
revisar el config.

```json
{
  "version": "2.0",
  "app_name": "to-do",
  "stages": {
    "dev": {
      "api_gateway_stage": "api"
    }
  }
}
```

revisar el app.py

```python
from chalice import Chalice

app = Chalice(app_name='to-do')


@app.route('/')
def index():
    return {'hello': 'world'}
```

levantarlo local
chalice local

Serving on http://127.0.0.1:8000

HTTP Method
URI Path
Description
GET
/todos/
Gets a list of all Todo’s
POST
/todos/
Creates a new Todo
GET
/todos/{id}
Gets a specific Todo
DELETE
/todos/{id}
Deletes a specific Todo
PUT
/todos/{id}
Updates the state of a Todo

esquema

```json
{
    "description": {"required": True, "type": "string"},
    "id": {"type": "string", "default_setter": lambda _: str(uuid4())},
    "state": {
        "type": "string",
        "allowed": ["uncompleted", "completed"],
        "default": "uncompleted",
    }
}
```

npm install -g aws-cdk
cdk --version
1.104.0 (build 44d3383)

