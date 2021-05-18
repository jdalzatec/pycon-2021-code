from cerberus import Validator
from chalice import Chalice, Response

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
        result = get_db().add_item(**body)
        if result:
            return Response(body={"result": "Item inserted"}, status_code=200)

        return Response(body={"error": "Item id already exists"}, status_code=400)

    return Response(body={"error": validator.errors}, status_code=400)


@app.route("/to-do/{todo_id}", methods=["GET"])
def read_todo(todo_id):
    result = get_db().get_item(todo_id)
    if result:
        return Response(body={"result": result}, status_code=200)

    return Response(body={"error": "Item not found"}, status_code=400)


@app.route("/to-do/{todo_id}", methods=["PUT"])
def update_todo(todo_id):
    body = app.current_request.json_body or {}
    if validator.validate(body, update=True):
        result = get_db().update_item(todo_id, **body)
        if result:
            return Response(body={"result": "Item updated"}, status_code=200)

        return Response(body={"error": "Item not found"}, status_code=400)

    return Response(body={"error": validator.errors}, status_code=400)


@app.route("/to-do/{todo_id}", methods=["DELETE"])
def delete_todo(todo_id):
    result = get_db().delete_item(todo_id)
    if result:
        return Response(body={"result": "Item deleted"}, status_code=200)

    return Response(body={"error": "Item not found"}, status_code=400)


@app.route("/to-do", methods=["GET"])
def read_all_todos():
    result = get_db().get_all_items()
    return Response(body={"result": result}, status_code=200)
