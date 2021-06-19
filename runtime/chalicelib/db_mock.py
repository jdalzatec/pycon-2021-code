from chalice import BadRequestError, NotFoundError

from chalicelib.crud import CRUD

DB = None


def get_db():
    global DB
    if not DB:
        DB = LocalDB()
    return DB


class LocalDB(CRUD):
    def __init__(self):
        self.db = {}

    def add_item(self, **body):
        item_id = body["id"]
        if item_id in self.db:
            raise BadRequestError("Item id already exists")

        self.db[item_id] = body
        return body

    def get_item(self, item_id):
        item = self.db.get(item_id)
        if not item:
            raise NotFoundError("Item not found")

        return item

    def update_item(self, item_id, **body):
        if not self.db.get(item_id):
            raise NotFoundError("Item not found")

        self.db[item_id] = {**self.db[item_id], **body}
        return self.db[item_id]

    def delete_item(self, item_id):
        if not self.db.get(item_id):
            raise NotFoundError("Item not found")

        return self.db.pop(item_id)

    def get_all_items(self, query=None):
        if not query:
            return [value for _, value in self.db.items()]

        return [
            value
            for _, value in self.db.items()
            if all([value.get(key) == val for key, val in query.items()])
        ]
