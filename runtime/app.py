from cerberus import Validator
from chalice import BadRequestError, Chalice, Response

from chalicelib.db_dynamo import get_db
from chalicelib.schema import SCHEMA

app = Chalice(app_name="to-do")

validator = Validator(SCHEMA)


@app.route("/")
def index():
    return {"hello": "world"}


@app.route("/to-do", methods=["POST"])
def create_todo():
    body = app.current_request.json_body or {}

    if validator.validate(body):
        body = validator.normalized(body)
        get_db().add_item(**body)
        return {"result": "Item inserted"}

    raise BadRequestError(str(validator.errors))


@app.route("/to-do/{todo_id}", methods=["GET"])
def read_todo(todo_id):
    result = get_db().get_item(todo_id)
    return {"result": result}


@app.route("/to-do/{todo_id}", methods=["PUT"])
def update_todo(todo_id):
    body = app.current_request.json_body or {}
    if validator.validate(body, update=True):
        get_db().update_item(todo_id, **body)
        return {"result": "Item updated"}

    raise BadRequestError(str(validator.errors))


@app.route("/to-do/{todo_id}", methods=["DELETE"])
def delete_todo(todo_id):
    get_db().delete_item(todo_id)
    return {"result": "Item deleted"}


@app.route("/to-do", methods=["GET"])
def read_all_todos():
    result = get_db().get_all_items()
    return {"result": result}


@app.route("/to-do/completed", methods=["GET"])
def read_all_completed_todos():
    result = get_db().get_all_items({"state": "completed"})
    return {"result": result}


@app.route("/to-do/uncompleted", methods=["GET"])
def read_all_uncompleted_todos():
    result = get_db().get_all_items({"state": "uncompleted"})
    return {"result": result}
